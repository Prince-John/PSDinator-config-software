"""

PSD hierarchical command generation.

PSD serial word requires:

       channels
       gain
       delay["range"] all
       width["range"] all
       vtc_range
       bias
       test_mode

PSD octal dac requires:

    any
    delay["dac_value"] any
    or
    width["dac_value"] any

PSD offset dac requires

       any
        channels["offset_dac"] any

PSD global enable requires:

        psd_global_enable
PSD trigger subcommands
    trigger_mode




"""