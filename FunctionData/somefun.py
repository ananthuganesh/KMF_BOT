#Importing Modules
import os
import time

#Creating Clear Console Funcation...
def console_clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

#Creating The Countdown Funcation...
def delay_counter(delay_time):
    while delay_time:
        mins, secs = divmod(delay_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\u001b[31;1mDelay Time Counter",timer, end="\r\u001b[0m")
        time.sleep(1)
        delay_time -= 1