# Importing Modules...
import os
import time
import sys
import random
from tqdm import tqdm
from instabot import Bot

# Importing My Modules & Functions...
from FunctionData.somefun import *
from FunctionData.USER_DATABase import *
from MokupData.mokupfun import *
from BotData.ConfiG import Option_Menu

# Bot Parameters
bot = Bot(
    max_likes_per_day=450,
    max_follows_per_day=300,
    max_unfollows_per_day=200,
    max_comments_per_day=100,
    max_messages_per_day=50,

    max_likes_to_like=10000000000,
    min_likes_to_like=10,

    max_followers_to_follow=500,
    min_followers_to_follow=100,
    max_following_to_follow=10,
    min_following_to_follow=2,
    min_media_count_to_follow=2,

    like_delay=random.randint(15, 30),
    follow_delay=20,
    unfollow_delay=20,
    comment_delay=20,
    message_delay=20,

    filter_users=False,
)


# Creating Instgram Automations Ideas...
def ig_teamhunter():  # Follow UnFollow Progress
    KMFHEADER()
    TEAMHUNDER()
    UserINP = input('Enter Target Username:- ')
    print("-------------------------------------------------------")
    while True:
        i = 1  # Number of Loop
        try:
            while i < 30:
                i += 1
                bot.follow(UserINP)
                delay_counter(240)
                bot.unfollow(UserINP)
                delay_counter(30)
        except KeyboardInterrupt:
            break
        delay_counter(1800)
    console_clear()
    Option_Menu()


def ig_rehash():  # Rehash in Post Progress
    KMFHEADER()
    REHASH()
    UserINP = input('Enter Post Link:- ')
    media_link = UserINP
    media_id = bot.get_media_id_from_link(media_link)
    while True:
        i = 1  # Number of Loop
        try:
            while i < 10:
                i += 1
                HASHTAG = random.choice(RE_HASH_TARGETS)
                bot.api.edit_media(media_id=media_id, captionText=HASHTAG)
                WAITING("FOR NEXT RE-HASH")
                delay_counter(3600)

        except KeyboardInterrupt:
            break
        delay_counter(1800)
    console_clear()
    Option_Menu()


def ig_hashliker():
    KMFHEADER()
    HASHLIKER()
    UserINP = input("Enter Target Hashtag:- ")
    HASHTAG_USERS = bot.get_hashtag_users(UserINP)
    bot.like_users(user_ids=HASHTAG_USERS, nlikes=3, filtration=False)
    delay_counter(800)
    console_clear()
    Option_Menu()


def ig_inshackle():
    KMFHEADER()
    INSHACKLE()
    while True:
        i = 1  # Number of Loop
        try:
            while i < 10:
                i += 1
                bot.follow_users(user_ids=INSHACKE_TARGETS, nfollows=10)
                WAITING('FOR UNFOLLOW')
                delay_counter(360)  # 6 min...
                bot.unfollow_users(user_ids=INSHACKE_TARGETS)
                WAITING('FOR NEXT FOLLOW')
                delay_counter(300)  # 5 min
        except KeyboardInterrupt:
            break
        delay_counter(1800)
    console_clear()
    Option_Menu()


def ig_unfollow():
    while True:
        try:
            bot.unfollow_non_followers(n_to_unfollows=30)
            delay_counter(300)
        except KeyboardInterrupt:
            break
    console_clear()
    Option_Menu()


def ig_bulkdm():
    KMFHEADER()
    BULK_GROUP_DM()
    UserINP = input("Enter Target Username:- ")
    MESSUserINP = input("Enter Message:- ")
    while True:
        i = 1  # Number of Loop
        try:
            while i < 3:
                i += 1
                TARGET_USERS = bot.get_user_followers(user_id=UserINP, nfollows=7)
                bot.send_message(text=MESSUserINP, user_ids=TARGET_USERS)
                delay_counter(random.randint(600,900))
        except KeyboardInterrupt:
            break
        delay_counter(1800)
    console_clear()
    Option_Menu()


def ig_likehash():
    KMFHEADER()
    LIKEHASTAG()
    UserINP = input("Enter Target Hashtag:- ")
    while True:
        i = 1  # Number of Loop
        try:
            while i < 30:
                i += 1
                bot.like_hashtag(hashtag=UserINP, amount=20)
                delay_counter(900)
        except KeyboardInterrupt:
            break
    console_clear()
    Option_Menu()


def ig_lchashtag():
    KMFHEADER()
    LIKE_COMMENT_BY_HASHTAG()
    UserINP = input("Enter Target Hashtag:- ")
    while True:
        MEDIAS = bot.get_hashtag_medias(hashtag=UserINP, filtration=False)
        i = 1  # Number of Loop
        try:
            while i < 20:
                i += 1
                ONEMEDIA = random.choice(MEDIAS)
                bot.like(media_id=ONEMEDIA)
                bot.comment(media_id=ONEMEDIA, comment_text=random.choice(COMMENT_S))
                delay_counter(120)
        except KeyboardInterrupt:
            break
        delay_counter(1800)
    console_clear()
    Option_Menu()


def ig_cmention():
    KMFHEADER()
    CMENTION()
    UserINP = input("Enter Target Hashtag:- ")
    ID = bot.get_hashtag_users(hashtag=UserINP)
    while True:
        MEDIAS = bot.get_hashtag_medias(hashtag=UserINP, filtration=False)
        i = 1  # Number of Loop
        try:
            while i < 6:
                i += 1
                HI = bot.get_username_from_user_id(random.choice(ID))
                ME = bot.get_username_from_user_id(random.choice(ID))
                UI = bot.get_username_from_user_id(random.choice(ID))
                AT = " @"
                PLUS = AT + ME + AT + HI + AT + UI
                ONEMEDIA = random.choice(MEDIAS)
                bot.comment(media_id=ONEMEDIA, comment_text=PLUS)
                bot.logger.info(msg="Mention in a Comment Done")
                delay_counter(200)

        except KeyboardInterrupt:
            break
        delay_counter(1800)
    console_clear()
    Option_Menu()
    

def ig_logout():
    KMFHEADER()
    LOGOUT()
    bot.logout()

def ig_fixbot():
    for i in tqdm(range(100), desc="Checking Issue..."):
        time.sleep(.1)
        pass
    bot.api.reinstall_app_simulation()
    bot.reset_counters()
    bot.reset_cache()
    for i in tqdm(range(100), desc="Fixing Issue..."):
        time.sleep(.2)
        pass
    console_clear()
    Option_Menu()


def ig_instruction():
    KMFHEADER()
    BOT_INSTRUCTIONS()
    USERInp = input("For Back Press 'b' and Hit Enter")
    if USERInp == "b":
        console_clear()
        Option_Menu()
    else:
        Option_Menu()
    console_clear()
    Option_Menu()

# ---------------------------------------------------------------------------------------------------------------

# Login Process
def Login():
    time.sleep(1)
    KMFHEADER()
    LOGIN()
    USERNAME = input("\u001b[32m[+]\u001b[0m Enter username:-")
    PASSWORD = input("\u001b[32m[+]\u001b[0m Enter password:-")
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    bot.login(username=USERNAME, password=PASSWORD, use_cookie=False)
    console_clear()


def MainBot():
    console_clear()
    Login()
    Option_Menu()