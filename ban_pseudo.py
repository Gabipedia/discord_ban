from discord.ext import commands
import discord
from time import sleep
from random import randint
import re

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

C_MAN_CHECK = "[CcKСс][Oo0ОоΟο][UuЦцυ][iIl1Ιι][lLIΙι][lLIΙι][eE3ΕεЕеЗз]"
H_MAN_CHECK = "[HhНнΗη][iIl1Ιι][TtТтΤτ]*[lLIΙι][eE3ΕεЕеЗз][Rr]"

def is_obscene_user(member):
    """Check if name, global_name or nick contain a forbidden word"""
    answer = False
    if re.search(C_MAN_CHECK, member.name):
        answer = True
    elif re.search(H_MAN_CHECK, member.name):
        answer = True
    elif re.search(C_MAN_CHECK, member.global_name):
        answer = True
    elif re.search(H_MAN_CHECK, member.global_name):
        answer = True
    elif re.search(C_MAN_CHECK, member.nick):
        answer = True
    elif re.search(H_MAN_CHECK, member.nick):
        answer = True
    else:
        answer = False
    return(answer)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
    """Check member who join the discord and ban him if his name contain forbidden words"""
    print("New member !")
    if is_obscene_user(member):
        print("Found the target !")
        try:
            #Get a random time between 4 and 8 minutes
            waiting_seconds = randint(240, 480)
            print(f"Banning the target in {waiting_seconds} seconds !")
            sleep(waiting_seconds)
            await member.ban(reason="Spam de photos obscènes")
        except:
            print("Couldn't ban the target :(")
    else:
        print("New member isn't the target...")

@bot.event
async def on_member_update(memberBefore,memberAfter):
    """Check member who update his profile and ban him if his name contain forbidden words"""
    print("Member update !")
    if is_obscene_user(memberAfter):
        print("Found the target !")
        try:
            #Get a random time between 10 and 30 seconds
            waiting_seconds = randint(10, 30)
            print(f"Banning the target in {waiting_seconds} seconds !")
            sleep(waiting_seconds)
            await member.ban(reason="Publication of obscene images !")
        except:
            print("Couldn't ban the target :(")
    else:
        print("This member isn't the target...")


bot.run('<your_bot_token_here>')
