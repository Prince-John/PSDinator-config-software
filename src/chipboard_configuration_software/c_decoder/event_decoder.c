
#include <assert.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <sys/poll.h>
#include <printf.h>
#include "event_decoder.h"


/** ******************************************
 *      Real time Event Decoder and Unpacker
 *  ******************************************
 *  This c program has the subroutines to decode the COBS encoded data stream from WashU CFD-PSD Chipboards
 *  and un-pack the data and assemble events.
 *
 *  This reads the incoming data stream from a named pipe which is written to by a separate UART reader thread.
 *
 *  This is intended to be used as a linked library by the Python based PSDinator Configuration Software.
 *  The unpacked ADC data is returned as an event struct to the python process to be plotted/processed.
 *
 *
 *
 *
 *  **************************
 *  **      Data Format     **
 *  **************************
 *
 *  There are 2 possible types of event packets that we can receive from the chipboard [as of firmware v0.4.0]
 *  depending on the received board id (always the first byte).
 *
 *  Note: Data Packets tagged with board_id = 255 are only generated if a board with board_id = 0 is present
 *   ---------------------------------
 *   1. ADC DATA if Board ID != 255
 *   ---------------------------------
 *    Byte #
 *      0     :  Board ID (0 - 63)
 *      1-4   :  Event number
 *      5     :  Channel number
 *      6     :  ADC A (low)
 *      7     :  ADC A (high)
 *      8     :  ADC B (low)
 *      9     :  ADC B (high)
 *      10    :  ADC C (low)
 *      11    :  ADC C (high)
 *      12    :  ADC T (low)
 *      13    :  ADC T (high)
 *      ----- : ------------  Only if more than one channel is triggered
 *      14    :  Channel number
 *      15    :  ADC A (low)
 *            :
 *        and so on...
 *            :
 *      148   :  ADC T (high) - Last possible byte if all 16 channels are hit.
 *  ---------------------------------
 *  2. Timestamp Data if Board ID = 255
 *  ---------------------------------
 *    Byte #  :
 *      0     :  Board ID = 255
 *      1-4   :  Event number
 *      5-11  :  Timestamp
 *
 * */


/** COBS decode data from buffer
	@param buffer Pointer to encoded input bytes
	@param length Number of bytes to decode
	@param data Pointer to decoded output data
	@return Number of bytes successfully decoded
	@note Stops decoding if delimiter byte is found
*/
size_t cobsDecode(const uint8_t *buffer, size_t length, void *data)
{
	assert(buffer && data);

	const uint8_t *byte = buffer; // Encoded input byte pointer
	uint8_t *decode = (uint8_t *)data; // Decoded output byte pointer

	for (uint8_t code = 0xff, block = 0; byte < buffer + length; --block)
	{
		if (block) // Decode block byte
			*decode++ = *byte++;
		else
		{
			block = *byte++;             // Fetch the next block length
			if (block && (code != 0xff)) // Encoded zero, write it unless it's delimiter.
				*decode++ = 0;
			code = block;
			if (!code) // Delimiter code found
				break;
		}
	}

	return (size_t)(decode - (uint8_t *)data);
}


int open_pipe(const char *path) {
    return open(path, O_RDONLY | O_NONBLOCK);
}

void close_pipe(int fd) {
    if (fd >= 0) {
        close(fd);
    }
}


/**
 * Unpack a regular ADC event packet from decoded COBS data.
 *
 * @param decoded Pointer to the decoded input buffer
 * @param len Length of the decoded buffer
 * @param out Pointer to the DecodedPacket struct where ADC data will be stored
 * @return 0 on success,
 *        -1 if the buffer length is invalid,
 *        -2 if multiplicity exceeds allowed channel count
 *
 * @note This function assumes event_number and board_id are already populated.
 *       Expects a sequence of 9-byte blocks starting at byte 5
 */

int unpack_regular_event(const uint8_t decoded[MAX_DECODED_PACKET_LEN], int len, DecodedPacket *out) {

    uint8_t multiplicity = (len - 5) / 9 ;

    if (multiplicity > MAX_ADC_CHANNELS) {
        return -2;  // Prevent buffer overflow
    }

    out->adc.num_channels = multiplicity;

    for (int i = 0, offset = 5; i < multiplicity; i++, offset += 9) {
        ADCReading *entry = &out->adc.channels[i];

        entry->channel = decoded[offset];

        entry->adc_a = (int16_t)((decoded[offset + 2] << 8) | decoded[offset + 1]);
        entry->adc_b = (int16_t)((decoded[offset + 4] << 8) | decoded[offset + 3]);
        entry->adc_c = (int16_t)((decoded[offset + 6] << 8) | decoded[offset + 5]);
        entry->adc_t = (int16_t)((decoded[offset + 8] << 8) | decoded[offset + 7]);
    }

    if ((len - 5) % 9 != 0) {
        return -1;  // Invalid length
    }

    return 0;
}


/**
* Unpack the special timestamp packet from decoded COBS data.
*
* @param decoded Pointer to the decoded input buffer (must be 12 bytes)
* @param len Length of the decoded buffer
* @param out Pointer to the DecodedPacket struct where the timestamp will be stored
* @return 0 on success, -1 if input length is invalid
*
* @note Assumes all other fields in the DecodedPacket are populated beforehand.
*       Copies 7 bytes starting from byte 5 into the 64-bit timestamp field.
*/
int unpack_timestamp_event(uint8_t decoded[MAX_DECODED_PACKET_LEN], int len, DecodedPacket *out) {

    if (len != 12){
        return -1;
    }

    uint64_t timestamp = 0;

    memcpy(&timestamp, decoded + 5, 7);

    out->timestamp.timestamp = timestamp;
    return 0;
}



/** Decode a single COBS-encoded chipboard packet into a structured DecodedPacket.
 *
 *  This function reads from the given file descriptor until a delimiter (0x00) is found.
 *  It then performs COBS decoding and unpacks the binary structure based on packet format.
 *
 *
 *
 * @param fd File descriptor from which to read the encoded packet stream
 * @param out Pointer to a DecodedPacket struct where the result will be stored
 * @param timeout_ms time in ms it waits for FIFO is to be ready
 * @return 0 if a valid packet was decoded successfully,
 *         -1 on I/O or decoding error,
 *         -2 timeout before packet read started - fifo not ready.
 *
 * @note This functions is blocking once the COBS packet read starts.
 *       This function Does not perform timestamp association or multi-board synchronization.
 */
int decode_next_event(int fd, DecodedPacket *out, int timeout_ms){
    int ret = -1;
    struct pollfd pfd;
    uint8_t cobs_buf[MAX_COBS_PACKET_LEN];
    uint8_t decoded[MAX_DECODED_PACKET_LEN];
    size_t packet_len = 0;
    uint8_t byte;

    pfd.fd = fd;
    pfd.events = POLLIN;

    int poll_result = poll(&pfd, 1, timeout_ms);

    if (poll_result == 0) {
        return -2;  // timeout, no data yet
    } else if (poll_result < 0) {
        return -1;
    }

    int result;
    // Blocking Read until 0x00
    int flags = fcntl(fd, F_GETFL, 0);
    //sets the blocking behaviour for reads from pipe.
    if (fcntl(fd, F_SETFL, flags & ~O_NONBLOCK) == -1){
        return -1;
    };

    while (1) {
        result = read(fd, &byte, 1);
        if (result == -1) {
            goto cleanup; // Restore flags before returning
        } else if (result == 0) {
            goto cleanup; // EOF - writer closed
        } else if (result == 1) {
            if (packet_len >= MAX_COBS_PACKET_LEN) break;
            cobs_buf[packet_len++] = byte;
            if (byte == 0) break;
        }
    }

    if (packet_len <= 2) return -1; // COBS packet cannot have less than 2 bytes

    // Start with unknown packet type
    out->type = PACKET_TYPE_UNKNOWN;

    int decoded_len = (int) cobsDecode(cobs_buf, packet_len, decoded);

    if (decoded_len < 5) return -1; // Incomplete decoded data packet, it will have at least board id and event number

    out->board_id = decoded[0];
    out->event_number = decoded[1] |
                        (decoded[2] << 8) |
                        (decoded[3] << 16) |
                        (decoded[4] << 24);

    if (out->board_id != TIMESTAMP_BOARD_ID) {
        out->type = PACKET_TYPE_ADC;
        unpack_regular_event(decoded, decoded_len, out);
    } else {
        out->type = PACKET_TYPE_TIMESTAMP;
        unpack_timestamp_event(decoded, decoded_len, out);

    }

    ret = 0;
    cleanup:
        if (fcntl(fd, F_SETFL, flags) == -1){
            return -1;
        };
        return  ret;
}




