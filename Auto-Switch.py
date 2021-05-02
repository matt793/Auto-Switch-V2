
# App works in collaboration with Putty network software. 
# The PyWinAuto module automates windows computers.
# This next line allows the Python program to open up other softwares automaticly.
from pywinauto.application import Application 

# This next line allows the Python program to control the keyboard.
from pywinauto.keyboard import send_keys 

# This next line/module allows the Python program to have time delays in between commands. 
from time import sleep

# This next line/module allows the Python program to read from a csv file.
import csv

# This next small block of will auto open the software Putty to be used by this program. 
# In order for this program to work, Putty has to be placed in the global PATH.
sleep(2) 
Application(backend="uia").start('putty') 
sleep(4) # This line means wait 4 seconds before next command.

# This next block of code autoruns through hotkeys, and text fills to get the user to the Cisco terminal. 
def start():
    with open('Cisco-Switch.csv') as csvDataFile:
        COM = list(csv.reader(csvDataFile)) # This and the next line help pull in the COM input data 
        locate = COM[1][12]
    # The COM input data must be adjusted in the csv file. You can find the COM number cell at column 13, row 2. 
    # Input your needed COM number there.

    send_keys('%{R}') # Hotkey alt+R will select serial option.
    sleep(1)
    send_keys('%{N}') # Hotkey alt+N will select COM field.
    sleep(1)
    send_keys('{BACKSPACE}') # Hotkey to clear current text in field.
    sleep(1)
    send_keys(f'COM{locate}')# F-string types command to input COM number with 'COM' text.
    send_keys('{ENTER}')
start()

# This next block of code programs your 48 switch ports.
def commands(c1, c2):
    # c1 pulls column info, c2 pulls row info.
    with open('Cisco-Switch.csv') as csvDataFile:
        data = list(csv.reader(csvDataFile))
        vlan = data[c1][c2] 
        ip = data[c1+1][c2]
        port = data[c1+2][c2]  

        # This next two lines tell the program to stop this block of code when it finds empty cells in the csv.
        if data == None or vlan == "":
            return  

        # Inputs Cisco commands with csv pulled data.
        sleep(2)
        send_keys('{ENTER}')
        sleep(1)
        send_keys('enable')
        send_keys('{ENTER}')
        sleep(1)
        send_keys('configure t',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(1)
        send_keys(f'vlan {vlan}',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(1)
        send_keys('exit')
        send_keys('{ENTER}')
        sleep(1)
        send_keys(f'interface vlan {vlan}',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(3)
        send_keys('{ENTER}')
        sleep(2)
        send_keys(f'ip address {ip}',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(1)
        send_keys(f'interface {port}',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(1)
        send_keys(f'switchport access vlan {vlan}',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(1)
        send_keys(f'do show running-config interface {port}',  with_spaces=True)
        send_keys('{ENTER}')
        sleep(1)
        send_keys('end')
        send_keys('{ENTER}')
        sleep(2)
        send_keys('{ENTER}')
        sleep(2)
        send_keys('copy running-config startup-config', with_spaces=True)
        sleep(1)
        send_keys('{ENTER}')
        sleep(1)
        send_keys('{ENTER}')
        sleep(3)
        send_keys('{ENTER}')
        sleep(1)
        send_keys('exit')
        send_keys('{ENTER}')
        sleep(3)
        send_keys('{ENTER}')
        sleep(1)
        send_keys('{ENTER}')

# These next two lines of code make a for loop with in a for loop. 
# This makes the program select the correct column and then the correct row
# in the correct order.        
for c1 in range(1, 25, 5): # If you added extra rows to the csv file change the #25 up.
    for c2 in range(1, 11, 1): # If you added extra columns to the csv file change the #11 up.
        commands(c1, c2)

# This next block of code shows the final work of the switch programing when you scroll up.
def show():
    sleep(1)
    send_keys('enable')
    send_keys('{ENTER}')
    sleep(1)
    send_keys('show vlan', with_spaces=True)
    send_keys('{ENTER}')
    sleep(7)
    send_keys('exit')
    send_keys('{ENTER}')     
show()