from FunctionData.somefun import *
from FunctionData.USER_DATABase import *
from MokupData.mokupfun import*


def Option_Menu():
    KMFHEADER()
    OPTION_LIST()
    while True:
        try:
            usrInp = input("\u001b[32m[+]\u001b[0m Enter Input:-")
            # If statment for option selection
            if usrInp == "1":
                console_clear()
                from BotData.MainBot import ig_teamhunter
                ig_teamhunter()

            if usrInp == "2":
                console_clear()
                Option_Menu()

            if usrInp == "3":
                console_clear()
                from BotData.MainBot import ig_cmention
                ig_cmention()

            if usrInp == "4":
                console_clear()
                from BotData.MainBot import ig_rehash
                ig_rehash()

            if usrInp == "5":
                console_clear()
                from BotData.MainBot import ig_inshackle
                ig_inshackle()

            if usrInp == "6":
                console_clear()
                from BotData.MainBot import ig_likehash
                ig_likehash()

            if usrInp == "7":
                console_clear()
                from BotData.MainBot import ig_hashliker
                ig_hashliker()

            if usrInp == "8":
                console_clear()
                from BotData.MainBot import ig_bulkdm
                ig_bulkdm()

            if usrInp == "9":
                console_clear()
                from BotData.MainBot import ig_lchashtag
                ig_lchashtag()

            if usrInp == "10":
                console_clear()
                from BotData.MainBot import ig_unfollow
                ig_unfollow()

            if usrInp == "11":
                console_clear()
                from BotData.MainBot import ig_fixbot
                ig_fixbot()

            if usrInp == "12":
                console_clear()
                from BotData.MainBot import ig_instruction
                ig_instruction()

            if usrInp == "13":
                console_clear()
                KMFHEADER()
                from BotData.MainBot import ig_logout
                ig_logout()
                
            else:
                console_clear()
                KMFHEADER()
                Option_Menu()
        except KeyboardInterrupt:
            break
    console_clear()
    OPTION_LIST()