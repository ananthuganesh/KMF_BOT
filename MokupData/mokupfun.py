import time
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Color and Codes
COLORS = { \
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
    "red-background": "\u001b[41m",
    "reset": "\u001b[0m",
}


def KMFHEADER():
    print("\u001b[34;1m   .----------------.  .----------------.  .----------------."), time.sleep(.1)
    print("   | .--------------. || .--------------. || .--------------. |"), time.sleep(.1)
    print("   | |  ___  ____   | || | ____    ____ | || |  _________   | |"), time.sleep(.1)
    print("   | | |_  ||_  _|  | || ||_   \  /   _|| || | |_   ___  |  | |"), time.sleep(.1)
    print("   | |   | |_/ /    | || |  |   \/   |  | || |   | |_  \_|  | |"), time.sleep(.1)
    print("   | |   |  __'.    | || |  | |\  /| |  | || |   |  _|      | |"), time.sleep(.1)
    print("   | |  _| |  \ \_  | || | _| |_\/_| |_ | || |  _| |_       | |"), time.sleep(.1)
    print("   | | |____||____| | || ||_____||_____|| || | |_____|      | |"), time.sleep(.1)
    print("   | |              | || |              | || |              | |"), time.sleep(.1)
    print("   | '--------------' || '--------------' || '--------------' |"), time.sleep(.1)
    print(
        "   '------\u001b[32mKERALA\u001b[0m\u001b[34;1m-------' '------\u001b[33;1mMALLU\u001b[0m\u001b[34;1m------' '---\u001b[31;1mFOLLOWERS\u001b[0m\u001b[34;1m---'."), time.sleep(
        .1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print(
        '                     (\u001b[31;1m●\u001b[0m__\u001b[31;1m●\u001b[0m) Version 2.0 (\u001b[31;1m●\u001b[0m__\u001b[31;1m●\u001b[0m)'), time.sleep(
        .1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[32mInstagram App API: Private                 YOUR IP:', IPAddr, '\u001b[0m')
    print('\u001b[33;1mOwner(s): @un_f_amour @_arun               Last Update: 30.5.2021\u001b[0m')
    print('\u001b[31;1mMaintainer(s): @mind________freezer        Telegram: ProjectX_insta\u001b[0m')


def TEAMHUNDER():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] T E A M H U N D E R\u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def REHASH():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] R E H A S H \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def UNFOLLOW_NON_FOLLOWERS():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] U N F O L L O W N O N - F O L L O W E R S \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def BULK_GROUP_DM():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] B U L K  G R O U P - D M\u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def HASHTAG_TARGETS():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] H A S H T A G - T A R G E T S \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def LIKEHASTAG():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] L I K E H A S T A G  \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def LIKE_COMMENT_BY_HASHTAG():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] L I K E & C O M M E N T B Y H A S H T A G\u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def GEOTAG_TARGETS():
    print('\u001b[33;1m--------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] G E O  T A G T A R G E T S \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def LIKE_COMMENT_BY_GEOTAG():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] L I K E C O M M E N T B Y G E O T A G \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def HASHLIKER():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] H A S H L I K E R \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def INSHACKLE():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] I N S H A C K L E \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def WAITING(Message_to):
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] W A I T I N G ', (Message_to), '\u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def CMENTION():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] C - M E N T I O N \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def LOGIN():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] L O G I N \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def LOGOUT():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] L O G O U T \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def ERROR():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] E R R O R \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def OPTION_LIST():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[32m[1]\u001b[0m TeamHunter                     \u001b[32m[8]\u001b[0m BULK_GROUP_DM'), time.sleep(.1)
    print('\u001b[32m[2]\u001b[0m Masslooker                     \u001b[32m[9]\u001b[0m Like,Comment Hashtag'), time.sleep(.1)
    print('\u001b[32m[3]\u001b[0m C-Mention                     \u001b[32m[10]\u001b[0m Unfollow Non-Followers'), time.sleep(.1)
    print('\u001b[32m[4]\u001b[0m Re-Hash                       \u001b[32m[11]\u001b[0m Fix Bot_Block'), time.sleep(.1)
    print('\u001b[32m[5]\u001b[0m Inshackle                     \u001b[32m[12]\u001b[0m Bot Instructions'), time.sleep(.1)
    print('\u001b[32m[6]\u001b[0m Like Hashtag                  \u001b[32m[13]\u001b[0m Logout'), time.sleep(.1)
    print('\u001b[32m[7]\u001b[0m HashLiker                      \u001b[32m[X]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def BOT_INSTRUCTIONS():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[31;1m[X] GIVE ONLY ONE TARGET A DAY ON TEAM-HUNTER\u001b[0m'), time.sleep(.1)
    print('\u001b[31;1m[X] RUN THE BOT ON THE SAME NETWORK\u001b[0m'), time.sleep(.1)
    print('\u001b[31;1m[X] AVOID VPN TO RUN BOT\u001b[0m'), time.sleep(.1)
    print('\u001b[31;1m[X] TRY TO RUN BOT CONTINUOYSLY\u001b[0m'), time.sleep(.1)
    print('\u001b[31;1m[X] USE HOOTSUITE APP FOR ACCOUNT SAFTY\u001b[0m'), time.sleep(.1)
    print('\u001b[31;1m[X] RUN BOT ONLY 15 HOURS\u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)


def KMF_OFFLINE():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] K M F  O F F L I N E \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('''                     \u001b[31;1m We'ill be back Soon!
Sorry for the inconvenience but we're performing some maintenance 
at the moment. We'll be back Online Shortly! \u001b[0m
                    
- \u001b[32mProject X Admin(s) - \u001b[0m'''), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)