Idea is to use a simple `ASCII` instruction set to send configuration commands to the FPGA on board for the actual configuration of the PSD and CFD chips.


Our syntax follows this simple structure, very loosely inspired by the SCPI standard. 


**GENERAL STRUCTURE**

TARGET_CHIP:TARGET_CHIP_SUBCOMMAND:VALUE

- `TARGET_CHIP`: Abstracted board component level chip not always actual IC's.
- `TARGET_CHIP_SUBCOMMAND` : This is optional and not present on for all chips
- `VALUE`: is the raw config value that will be interpreted as binary data and loaded into the chip, it is encoded in hex but sent as ASCII representation.  

### Top level - Command Type


