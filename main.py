#Importing Modules
import requests

#Importing Mi Func...
from FunctionData.somefun import console_clear
from MokupData.mokupfun import *
from BotData.MainBot import MainBot

#Status
KMFstatus = ("online")
KMFstatuschecker = requests.get('https://docs.google.com/spreadsheets/d/1j6DdU1fU36cWzP9rjxrSYV-tX5pW7Ard2m_66nGdzWw/edit?usp=sharing')

#Program Started
if KMFstatus in KMFstatuschecker.text:
    MainBot()
else:
    KMFHEADER()
    KMF_OFFLINE()