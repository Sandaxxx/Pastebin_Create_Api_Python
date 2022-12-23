import pastebinapi
import os 
import time  
import requests
from colorama import init
init()
from colorama import Fore, Back, Style


banner = """
  ██████  ▄▄▄       ███▄    █ ▓█████▄  ▄▄▄      ▒██   ██▒
▒██    ▒ ▒████▄     ██ ▀█   █ ▒██▀ ██▌▒████▄    ▒▒ █ █ ▒░
░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██  ▀█▄  ░░  █   ░
  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██  ░ █ █ ▒ 
▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓  ▓█   ▓██▒▒██▒ ▒██▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░▒▒ ░ ░▓ ░
░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░░   ░▒ ░
░  ░  ░    ░   ▒      ░   ░ ░  ░ ░  ░   ░   ▒    ░    ░  
      ░        ░  ░         ░               ░  ░      ░                                 
"""


while True:
  print(Fore.MAGENTA+banner)
  print(Fore.RED+"┌―――――┬――――――――――――――――――――――――――――――――――┐")
  print("| [1] | ✶ "+Fore.GREEN+"Connect Account  "+Fore.RED+"              |")         
  print("| [2] | ✶ Create Pastebin                |")                
  print("| [3] | ✶ Text From URL Pastebin         |")    
  print("| [4] | ✶ Crédit                         |")
  print("└―――――┴――――――――――――――――――――――――――――――――――┘")
  print(Fore.YELLOW)
  print(Fore.YELLOW)
  print(Fore.YELLOW)
  

  #  For select choice  
  choice = input("Entrer choice : ")
  print()
  print()
  os.system('cls')


# ┌⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┐


    # LOGIN ACCOUNT PASTEBIN DEVELOPPER
     
  if (choice == "1"):
    print(Fore.GREEN+'Login Your Account Pastebin Developper')
    print(Fore.YELLOW)
    username = input("Your Username : ")
    password = input("Your Password : ")
    api_key = input("Your API key : ")
    print(Fore.CYAN)
    pastebinapi.check(username, password, api_key)
    print(Fore.MAGENTA+' [+] NOW SELECT OPTION 2')
    time.sleep(5)
    os.system('cls')



    # CREATE PASTEBIN

  if (choice == "2"):
    print('')
    print(Fore.GREEN+'')
    title_pastebin = input(" [>] - Enter the title : ")
    content_pastebin = input(" [>] - Enter the text : ")
    privacity = "1" #       0 = public  1 = unlisted 
    pastebinapi.paste(username, password, api_key, privacity, title_pastebin, content_pastebin)
    time.sleep(15)
    os.system('cls')


    # READ TEXT FORM PASTEBIN TO URL

  if (choice == "3"):
    print(Fore.GREEN+'Read Text URL(raw) Pastebin | ex. https://pastebin.com/raw/exemple')
    print()
    print(Fore.RED)

    url_pastebin = input("Enter url pastebin : ")
    response = requests.get(url_pastebin).text
    os.system('cls')
    print(Fore.BLUE+'Content : \n\n\n'+Fore.WHITE+response)
    time.sleep(50)



    # CREDIT DEVELOPPER SANDAX 
  if (choice == "4"):
    print(Fore.MAGENTA+'       Developped by Sandax'+Fore.YELLOW+'\n       Github : https://github.com/Sandaxxx/Pastebin_Create_Api_Python ')
    time.sleep(5)


