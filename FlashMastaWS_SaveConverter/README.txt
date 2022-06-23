The official menu has some problems with how it loads some games so you can avoid these problems by just flashing the rom to "Slot 1" in the official flashmasta.exe software: https://www.flashmasta.com/software-downloads/

My software aims to prepare a generic WonderSwan Save for use with a "Flash Masta" flashcart.

All the program does, is find the length of your save file (eg:32,768 bytes) and divide that by 4,194,304 bytes (the size of the Flash Masta's generated save file).  
I imagine there's only a single chunk of the massive 4mb that needs to be modified, but I couldn't figure out which chunk that was.
I didn't notice any adverse affects by just duplicating the save file 128 times :)

To use the tool:

- Flash a game to Slot 1 using the official Flash Masta software
- Find a save file for a Wonder Swan game you want to put onto the Flash Masta
- Run the FlashMastaWS_SRAMconverter.exe GUI to convert the file to make it Flash Masta Readable
- Back on the official Flash Masta software, Consider making a backup of your Flash Masta's save data by pressing "Backup Save Data"
- click "Restore Save Data" and navigate to the file that was created "Menuless_Save.wsf"

I only tested this with 32kb game but it should work for any size game.


