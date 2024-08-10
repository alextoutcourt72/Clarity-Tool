import os
from os import system

import requests
from pystyle import Colors, Colorate, Center

def update_checker():
    try:
        response = requests.get("https://api.github.com/repos/Al3xUI/clarity-tool/releases/latest")
        data = response.json()
        latest_version = data["tag_name"]
        current_version = open("version.txt", "r").read()
        if latest_version != current_version:
            print(f"A new version of Clarity tool is available: {latest_version}")
            print("Do you want to update now? (y/n)")
            choice = input()
            if choice.lower() == "y":
                os.system("git clone https://github.com/Al3xUI/clarity-tool.git")
                os.system("cd clarity-tool")
                os.system("setup.bat")
                os.system("python main.py")
            else:
                print("Update cancelled.")
        else:
            print("You are using the latest version of Clarity tool.")
    except:
        print("Failed to check for updates.")

title = "Clarity tool \ made by alex \ v1.0"
system("title " + title)

os.system('cls' if os.name == 'nt' else 'clear')

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

                                                Made with <3 By Alex            ╔═════════════════════════════════════╗                 
                                                    version 1.0                 ║                [!]                  ║
                                                          ╦                     ║     clarity ne vous demendera       ║
                                                          ║                     ║ jamais vos ainformations perssonels.║
                                                          ║                     ╚════════════════╦════════════════════╝
                               ╔══════════════════════════╩════════════════════════╗             ║ 
                               ║                                                   ║             ║                 
        ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩═════════════╩════════╗
        ║   [1] > Tool info                             ║ ║   [10] > Linkvertise bypasser                 ║
        ║   [2] > Ip tools                              ║ ║   [11] > ClarityAI (in dev)                   ║
        ║   [3] > N/A                                   ║ ║   [12] > Self Security (in dev)               ║
        ║   [4] > OSINT Framework (website)             ║ ║   [13] >                                      ║ 
        ║   [5] > Check Phone Number                    ║ ║   [14] >                                      ║
        ║   [6] > PC Info                               ║ ║   [15] >                                      ║
        ║   [7] > Discord token info                    ║ ║   [16] >                                      ║ 
        ║   [8] > Username Tracker                      ║ ║   [17] >                                      ║ 
        ║   [9] > Discord server info                   ║ ║   [18] >                                      ║          
        ╚═══════════════════════════════════════════════╝ ╚═══════════════════════════════════════════════╝        
"""
print(Colorate.Horizontal(Colors.blue_to_purple, menu))

choice = int(input(Colorate.Horizontal(Colors.blue_to_purple, 'Choose >> ')))


def execute_script(choice):
    if choice == 1:
        os.system('python ./modules/tool_info.py')
    elif choice == 2:
        os.system('python ./modules/ip_lookup.py')
    elif choice == 3:
        os.system('python ./main.py')
    elif choice == 4:
        os.system('python ./modules/osint_tool.py')
    elif choice == 5:
        os.system('python ./modules/number_info.py')
    elif choice == 6:
        os.system('python ./modules/PC_info.py')
    elif choice == 7:
        os.system('python ./modules/discord_token_info.py')
    elif choice == 8:
        os.system('python ./modules/username_tracker.py')
    elif choice == 9:
        os.system('python ./modules/discord_server_info.py')

execute_script(choice)
