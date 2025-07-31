#ifndef EVENT_DECODER_H
#define EVENT_DECODER_H

#include <stdint.h>

#define MAX_ADC_CHANNELS 16
#define TIMESTAMP_BOARD_ID 255
#define MAX_COBS_PACKET_LEN 255
#define MAX_DECODED_PACKET_LEN 253


typedef enum {
    PACKET_TYPE_ADC,
    PACKET_TYPE_TIMESTAMP,
    PACKET_TYPE_UNKNOWN
} PacketType;

typedef struct {
    uint8_t channel;
    int16_t adc_a;
    int16_t adc_b;
    int16_t adc_c;
    int16_t adc_t;
} ADCReading;

typedef struct {
    PacketType type;
    uint8_t board_id;
    uint32_t event_number;

    union {
        struct {
            uint8_t num_channels;
            ADCReading channels[MAX_ADC_CHANNELS];
        } adc;

        struct {
            uint64_t timestamp;
            float timestamp_ns;
        } timestamp;
    };
} DecodedPacket;


int open_pipe(const char *path);  // returns file descriptor
void close_pipe(int fd);
int decode_next_event(int fd, DecodedPacket *out, int timeout_ms);  // 0 = OK, -1 = error, -2 = timeout
int unpack_regular_event(const uint8_t decoded[MAX_DECODED_PACKET_LEN], int len, DecodedPacket *out);
int unpack_timestamp_event(uint8_t decoded[MAX_DECODED_PACKET_LEN], int len, DecodedPacket *out);
size_t cobsDecode(const uint8_t *buffer, size_t length, void *data);



#endif
