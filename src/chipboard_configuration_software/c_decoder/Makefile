CC = gcc
CFLAGS = -Wall -O2 -fPIC
TARGET = libevent_decoder.so

all: $(TARGET)

$(TARGET): event_decoder.c event_decoder.h
	$(CC) $(CFLAGS) -shared -o $(TARGET) event_decoder.c

clean:
	rm -f *.o *.so

.PHONY: all clean
