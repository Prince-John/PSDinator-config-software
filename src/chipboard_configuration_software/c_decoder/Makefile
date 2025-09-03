CC = gcc
CFLAGS = -Wall -Wextra -Werror -O2 -fPIC -std=gnu11 -pedantic
TARGET = libevent_decoder.so

# Add a test to verify BSD types cause errors
test-portability:
	@echo "Testing for BSD type usage..."
	@if grep -q "u_int64_t\|u_int32_t\|u_int16_t\|u_int8_t" event_decoder.c event_decoder.h 2>/dev/null; then \
		echo "ERROR: Found BSD types (u_int*_t) in code. Use standard uint*_t types instead."; \
		grep -n "u_int64_t\|u_int32_t\|u_int16_t\|u_int8_t" event_decoder.c event_decoder.h; \
		exit 1; \
	else \
		echo "✓ No BSD types found"; \
	fi
all: $(TARGET)

$(TARGET): event_decoder.c event_decoder.h
	$(CC) $(CFLAGS) -shared -o $(TARGET) event_decoder.c

clean:
	rm -f *.o *.so

.PHONY: all clean
