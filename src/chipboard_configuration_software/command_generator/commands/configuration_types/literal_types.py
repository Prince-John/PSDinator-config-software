from typing import Literal

SubchannelKey = Literal["a", "b", "c"]
BoolStr = Literal["True", "False"]
ChannelKey = Literal[
    "0", "1", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "11", "12", "13", "14", "15"
]
ChipboardConfigurationDictKey = Literal["cfd", "psd", "mux", "delay"]
PreampOutputKey = Literal["disabled", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
OrOutputKey = Literal["cfd", "psd_0", "psd_1", "psd_0_or_psd_1"]
IntxOutputKey = Literal["psd_0", "psd_1"]
PsdCfdOutputKey = Literal["psd_0", "psd_1"]