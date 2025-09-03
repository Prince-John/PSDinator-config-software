"""
C decoder module for high-performance event decoding.

This module provides access to C-based event decoding functions for performance-critical
operations. The C extension is built automatically on first import if not already available.
"""
from chipboard_configuration_software.c_decoder.c_extension_loader import load_event_decoder, ensure_c_extension_built

# Pre-load the extension when the module is imported
try:
    event_decoder_lib = load_event_decoder()
    print("C event decoder extension loaded successfully")
except Exception as e:
    print(f"Warning: Failed to load C event decoder extension: {e}")
    print("Falling back to Python implementation if available")
    event_decoder_lib = None

__all__ = ['event_decoder_lib', 'load_event_decoder', 'ensure_c_extension_built']
