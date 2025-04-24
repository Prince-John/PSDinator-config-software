from typing import TypedDict, Literal, Dict
from .literal_types import *

# Predefined allowed literals
BIAS_MODES = Literal["high", "low"]
POLARITY_MODES = Literal["positive", "negative"]
VTC_RANGES = Literal["250 ns", "2 us"]
SUBCHANNEL_RANGES = Literal[0, 1, 2, 3, "0", "1", "2", "3"]
BOOL_TYPES = Literal["True", "False"]

# Define types for each subfield
ChannelEnableDict = Dict[ChannelKey, BOOL_TYPES]


class RangeDict(TypedDict):
    a: SUBCHANNEL_RANGES
    b: SUBCHANNEL_RANGES
    c: SUBCHANNEL_RANGES


class SerialRegisterSettingsDict(TypedDict):
    polarity: POLARITY_MODES
    bias: BIAS_MODES
    gain: Dict[str, int]  # gain values are integers (e.g., "500", "10000")
    vtc_range: VTC_RANGES
    delay_ranges: RangeDict
    width_ranges: RangeDict
    channel_enables: ChannelEnableDict


class OctalDacSettingsDict(TypedDict):
    delay_voltages: RangeDict
    width_voltages: RangeDict
    auto_veto_time: str  # Can be a string but should be a number
    multiplicity_offset: str  # Same here


class SubchannelOffsetDacDict(TypedDict, total=False):
    a: str
    b: str
    c: str


ChannelOffsetDacDict = Dict[ChannelKey, SubchannelOffsetDacDict]


class TestModeDict(TypedDict):
    status: Literal["on", "off"]
    channel: ChannelKey
    subchannel: SubchannelKey


# Top-level configuration
class PSDConfigurationDict(TypedDict, total=False):
    global_enable: Literal["True", "False"]
    test_mode: TestModeDict
    serial_register_settings: SerialRegisterSettingsDict
    octal_dac_settings: OctalDacSettingsDict
    trigger_mode: Literal["1", "2", "3"]
    channel_offset_dacs: ChannelOffsetDacDict
