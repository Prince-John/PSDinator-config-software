import numpy as np

from chipboard_configuration_software.c_decoder import event_decoder_lib
from ctypes import Structure, Union, c_uint8, c_int16, c_uint32, c_uint64, c_float, c_int, POINTER, c_char_p

from numpy.ctypeslib import ndpointer




MAX_ADC_CHANNELS = 16

PACKET_TYPE_ADC = 0
PACKET_TYPE_TIMESTAMP = 1
PACKET_TYPE_UNKNOWN = 2

lib = event_decoder_lib


# Match `typedef struct ADCReading`
class ADCReading(Structure):
    _fields_ = [
        ("channel", c_uint8),
        ("adc_a", c_int16),
        ("adc_b", c_int16),
        ("adc_c", c_int16),
        ("adc_t", c_int16),
    ]


# for numpy converstion from ctypes
adc_reading_np_dtype = np.dtype([
    ("channel", np.uint8),
    ("adc_a", np.int16),
    ("adc_b", np.int16),
    ("adc_c", np.int16),
    ("adc_t", np.int16),
], align=True)


class ADCData(Structure):
    _fields_ = [
        ("num_channels", c_uint8),
        ("channels", ADCReading * MAX_ADC_CHANNELS)
    ]


class TimestampData(Structure):
    _fields_ = [
        ("timestamp", c_uint64),
        ("timestamp_ns", c_float)
    ]


class PacketUnion(Union):
    _fields_ = [
        ("adc", ADCData),
        ("timestamp", TimestampData)
    ]


class DecodedPacket(Structure):
    _fields_ = [
        ("type", c_int),  # enum, maps to int
        ("board_id", c_uint8),
        ("event_number", c_uint32),
        ("data", PacketUnion),  # union field
    ]


decode_next_event = lib.decode_next_event
decode_next_event.argtypes = [c_int, POINTER(DecodedPacket), c_int]
decode_next_event.restype = c_int

# some_dll.f.argtypes = [ndpointer(numpy.uint8, flags="C_CONTIGUOUS"),
#                        ctypes.c_size_t]
# some_dll.f.restype = None



# int open_pipe(const char *path)
lib.open_pipe.argtypes = [c_char_p]
lib.open_pipe.restype = c_int

# void close_pipe(int fd)
lib.close_pipe.argtypes = [c_int]
lib.close_pipe.restype = None
