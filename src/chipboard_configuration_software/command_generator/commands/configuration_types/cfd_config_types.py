from typing import TypedDict, Literal, Dict, Optional

from .literal_types import *

# --- Literals for enums and fixed options ---

NowlinMode = Literal["short", "long"]
NowlinDelay = Literal[
    "1 ns", "2 ns", "3 ns", "4 ns", "5 ns", "6 ns", "7 ns", "8 ns", "9 ns", "10 ns", "11 ns", "12 ns", "13 ns", "14 ns",
    "15 ns", "16 ns", "24 ns", "36 ns", "48 ns", "60 ns", "72 ns", "84 ns", "96 ns",
    "108 ns", "120 ns", "132 ns", "144 ns", "156 ns", "168 ns", "180 ns", "192 ns"]
LockoutMode = Literal["short", "long", "disabled"]
TestPoint = Literal[
    "AVSS",
    "lockout pulse",
    "leading edge detector pulse",
    "oneshot input",
    "oneshot pulse",
    "zero cross detector pulse"
]
AgndTrim = Literal[
    "1.36 V", "1.43 V", "1.49 V", "1.56 V",
    "1.63 V", "1.69 V", "1.77 V", "1.84 V"
]

CFDWidths = Literal["50", "100", "200", "500"]



# --- Options dictionaries (optional if you want to validate mapping) ---
AgndTrimOptions = Dict[AgndTrim, int]
TestPointOptions = Dict[TestPoint, int]


# --- Common Settings Block ---
class CfdCommonSettingsDict(TypedDict):
    nowlin_mode: NowlinMode
    nowlin_delay: NowlinDelay
    lockout_DAC: str
    lockout_mode: LockoutMode
    cfd_pulse_width: CFDWidths
    agnd_trim: AgndTrim
    agnd_trim_options: Optional[AgndTrimOptions]
    global_Mode: BoolStr
    le_out_enable: BoolStr
    test_point: TestPoint
    test_point_options: TestPointOptions
    test_point_channel: ChannelKey
    negative_polarity: BoolStr


# --- Per-channel Settings Block ---
class CfdIndividualChannelSettingsEntry(TypedDict):
    enable: BoolStr
    leading_edge_DAC_value: int
    sign_bit: BoolStr


CfdIndividualChannelSettingsDict = Dict[ChannelKey, CfdIndividualChannelSettingsEntry]


# --- Final CFD Config Block ---
class CFDConfigurationDict(TypedDict):
    common_settings: CfdCommonSettingsDict
    individual_channel_settings: CfdIndividualChannelSettingsDict
    global_enable: BoolStr
