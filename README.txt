![alt text](/Screenshot-1.png?raw=true "FlashMastaWS_SRAMconverter")

The official Menu ROM has some problems with how it loads some games. You can avoid the menu rom entirely and these problems by just flashing a single game's ROM to "Slot 1" by using the official flashmasta.exe software: https://www.flashmasta.com/software-downloads/

My software aims to prepare a WonderSwan save for use with a "Flash Masta" flashcart.

The hacky way it works, is it finds the length of your save file (eg:32,768 bytes) and divides that into 4,194,304 bytes (the size of the Flash Masta's generated save file).  Then it just copies the content and loops through by the number of times found.
I imagine there's only a single chunk of the massive 4MB that actually needs to be modified, but I couldn't figure it out because for whatever reason the flashcart writes the save to 8(?) different chunks on the SRAM.
I didn't notice any adverse affects by just duplicating the save file 128 times so that's my solution :)

To use the tool:

- Download the FlashMastaWS_SRAMconverter.exe by goin to releases https://github.com/Churchdill/FlashMasta-Slot1-Save-Converter/releases/tag/1.0
- Flash a game to Slot 1 using the official Flash Masta software
- Find a save file for a Wonder Swan game you want to put onto the Flash Masta
- Run the FlashMastaWS_SRAMconverter.exe GUI to convert the file to make it Flash Masta Readable
- Back on the official Flash Masta software, Consider making a backup of your Flash Masta's save data by pressing "Backup Save Data"
- click "Restore Save Data" and navigate to the file that was created "Menuless_Save.wsf"

I only tested this with 32KB game but it should work for any size game.


