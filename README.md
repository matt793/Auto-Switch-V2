# Auto-Switch-V2
Program a Cisco-Switch with a spreadsheet, and then walkaway to take care of other things: while Auto-Switch automates the work. The program works by automating your keyboard and opening up PuTTY network software.

## Getting Started
The first thing you will need is the software PuTTY. Auto-Switch works by automating PuTTY and the Cisco switch language. 
After installing PuTTY, then `place the PuTTY software to your global PATH`!

Auto-Switch can now run out of the gate perfectly as is. It is now up to you how you want to set up your CSV database.
This repo will come a pre-set templet CSV file of pre-set date. You can then edit the file to your ideal setup. 

## COM Edit
In order to gane access to a Cisco terminal serial, you must have the correct COM number inputed. 
Find out what yours is by looking it up in your `Device Manager` under your connected `COM port driver`.
After you find the correct COM number, input it into the CSV database cell. You can find the needed cell at column 13, row 2.

![Example](/Gifs/Edit-COM.gif "Example")

## Desktop Icon
The provided Appcation .exe file needs to stay inside the main folder, however, you can create a shortcut to the .exe file by right clicking on it and selecting `create shortcut`.
You can then drag the shortcut to your desktop.

![Example](/Gifs/Desktop-Icon.gif "Example")

## Demo 
Here's a short gif clip of the software automating the PuTTY opening, and some Cisco commands.

![Example](/Gifs/Demo.gif "Example")

## Special Thanks
I would like to give a special thanks to @sdixon5 who helped my out with the for loop with in a for loop part of my code. Big fix. 
