import os
from os import system

title="Clarity tool \ made by alex \ v1.0.0"
system("title "+title)

os.system('color D')
os.system('cls')


menu = """
             ▄████▄   ██▓    ▄▄▄       ██▀███   ██▓▄▄▄█████▓▓██   ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
            ▒██▀ ▀█  ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
            ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
            ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
            ▒ ▓███▀ ░░██████▒▓█   ▓██▒░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
            ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
              ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
            ░          ░ ░    ░   ▒     ░░   ░  ▒ ░  ░       ▒ ▒ ░░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
            ░ ░          ░  ░     ░  ░   ░      ░            ░ ░                     ░ ░      ░ ░      ░  ░
            ░                                                ░ ░                                           

                                                    Made by Alex
                                                    version 1.0.0
Select tool :

        [1] Tool info       [6] PC info
        [2] Ip lookup       [7] Discord Token Info
        [3] Whois lookup    [8] Username Tracker
        [4] OSINT           [9] discord server info    
        [5] Web page saver (not work)
"""
print(menu)

choice = int(input('Choose >> '))

def execute_script(choice):
    if choice == 1:
        os.system('python ./modules/tool_info.py')
    elif choice == 2:
        os.system('python ./modules/ip_lookup.py')
    elif choice == 3:
        os.system('python ./modules/whois_lookup.py')
    elif choice == 4:
        os.system('python ./modules/osint_tool.py')
    elif choice == 5:
        os.system('python main.py')
    elif choice == 6:
        os.system('python ./modules/PC_info.py')
    elif choice == 7:
        os.system('python ./modules/discord_token_info.py')
    elif choice == 8:
        os.system('python ./modules/username_tracker.py')
    elif choice == 9:
        os.system('python ./modules/discord_server_info.py')

execute_script(choice)
