import os
import subprocess
import sys
from pathlib import Path
import ctypes
import threading

_build_lock = threading.Lock()
_extension_checked = False


def ensure_c_extension_built():
    """
    Ensure the C extension is built and available.
    This function is thread-safe and will only attempt to build once.

    :return: Path to the .so file
    :raises: RuntimeError if the extension cannot be built or found
    """
    global _extension_checked

    with _build_lock:
        if _extension_checked:
            return get_so_path()

        so_path = get_so_path()

        # Check if .so file already exists
        if so_path.exists():
            try:
                # Try to load it to verify it's valid
                ctypes.CDLL(str(so_path))
                _extension_checked = True
                return so_path
            except OSError:
                print(f"Warning: Existing .so file {so_path} is invalid, rebuilding...")

        # Build the extension
        build_c_extension()

        # Verify it was built successfully
        if not so_path.exists():
            raise RuntimeError(f"C extension build failed - {so_path} not found")

        try:
            ctypes.CDLL(str(so_path))
        except OSError as e:
            raise RuntimeError(f"Built C extension is invalid: {e}")

        _extension_checked = True
        return so_path


def get_so_path():
    """
    Get the expected path to the .so file.

    :return: Path object pointing to the expected location of libevent_decoder.so
    """
    current_dir = Path(__file__).parent
    return current_dir / "libevent_decoder.so"


def get_c_decoder_dir():
    """
    Get the path to the c_decoder directory.

    :return: Path object pointing to the c_decoder directory
    """
    return Path(__file__).parent


def build_c_extension():
    """
    Build the C extension using the Makefile.

    :raises: RuntimeError if the build fails or required tools are missing
    """
    c_decoder_path = get_c_decoder_dir()
    makefile_path = c_decoder_path / "Makefile"

    if not makefile_path.exists():
        raise RuntimeError(f"Makefile not found at {makefile_path}")

    print(f"Building C extension in {c_decoder_path}")

    # Check for required build tools
    try:
        subprocess.run(["make", "--version"],
                       capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise RuntimeError("make is not available. Please install build tools.")

    try:
        subprocess.run(["gcc", "--version"],
                       capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise RuntimeError("gcc is not available. Please install a C compiler.")

    # Change to the c_decoder directory and run make
    original_cwd = os.getcwd()
    try:
        os.chdir(c_decoder_path)

        # Clean previous builds
        result = subprocess.run(["make", "clean"],
                                capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Warning: make clean failed: {result.stderr}")

        # Build
        result = subprocess.run(["make"],
                                capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Make failed: {result.stderr}")

        print("C extension built successfully")
        if result.stdout:
            print(result.stdout)

    finally:
        os.chdir(original_cwd)


def load_event_decoder():
    """
    Load the event decoder C library.

    :return: ctypes.CDLL object for the loaded library
    :raises: RuntimeError if the library cannot be built or loaded
    """
    so_path = ensure_c_extension_built()
    return ctypes.CDLL(str(so_path))


def get_event_decoder_lib():
    """
    Get the event decoder library (builds if necessary).

    :return: ctypes.CDLL object for the event decoder library
    :raises: RuntimeError if the library cannot be built or loaded
    """
    return load_event_decoder()
