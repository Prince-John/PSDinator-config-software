from chipboard_configuration_software.c_decoder import event_decoder_lib
from ctypes import c_int, POINTER, c_char_p

from visualizer_app.data.decoder_types import DecodedPacket

lib = event_decoder_lib


decode_next_event = lib.decode_next_event
decode_next_event.argtypes = [c_int, POINTER(DecodedPacket), c_int]
decode_next_event.restype = c_int

# int open_pipe(const char *path)
lib.open_pipe.argtypes = [c_char_p]
lib.open_pipe.restype = c_int

# void close_pipe(int fd)
lib.close_pipe.argtypes = [c_int]
lib.close_pipe.restype = None


def open_named_pipe(path: str) -> int:
    return lib.open_pipe(path.encode('utf-8'))


def close_named_pipe(fd: int):
    lib.close_pipe(fd)