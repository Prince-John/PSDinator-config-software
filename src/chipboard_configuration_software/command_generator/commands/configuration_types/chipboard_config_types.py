from typing import TypedDict, Dict

from .cfd_config_types import CFDConfigurationDict
from .psd_config_types import PSDConfigurationDict
from .literal_types import *


class DelayEntry(TypedDict):
    value: str


DelayConfigurationDict = Dict[ChannelKey, DelayEntry]


class MuxConfigurationDict(TypedDict):
    preamp_output: PreampOutputKey
    or_output: OrOutputKey
    intx_output: IntxOutputKey
    psd_cfd_output: PsdCfdOutputKey


# --- Top-level Configuration ---
class ChipboardConfigurationDict(TypedDict):
    chipboard_number: int
    chipboard_mode: str
    cfd: CFDConfigurationDict
    psd: PSDConfigurationDict
    delay: DelayConfigurationDict
    mux: MuxConfigurationDict
