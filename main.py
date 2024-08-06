import os
from os import system

title="Clarity tool \ made by alex \ v1.0.0"
system("title "+title)

os.system('color D')
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

                                                    Made by Alex
                                                    version 1.0
                                                          ╦
                                                          ║
                                        ╔═════════════════╩════════════════╗
                                        ║               [!]                ║
                                        ║ Clarity ne vous demendera jamais ║
                                        ║    vos informations perssonels.  ║
                                        ╚═════════════════╦════════════════╝
                                                          ║
                               ╔══════════════════════════╩════════════════════════╗
                               ║                                                   ║                              
        ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩══════════════════════╗ 
        ║   [1] > Tool info                             ║ ║   [10] > Discord server info                  ║
        ║   [2] > Ip tools                              ║ ║   [11] >                                      ║
        ║   [3] > Whois lookup                          ║ ║   [12] >                                      ║
        ║   [4] > OSINT Framework (website)             ║ ║   [13] >                                      ║ 
        ║   [5] > Check Phone Number                    ║ ║   [14] >                                      ║
        ║   [6] > PC Info                               ║ ║   [15] >                                      ║
        ║   [7] > Discord token info                    ║ ║   [16] >                                      ║ 
        ║   [8] > Username Tracker                      ║ ║   [17] >                                      ║ 
        ║   [9] > Linkvertise Bypasser                  ║ ║   [18] >                                      ║          
        ╚═══════════════════════════════════════════════╝ ╚═══════════════════════════════════════════════╝        
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
        os.system('python ./modules/number_info.py')
    elif choice == 6:
        os.system('python ./modules/PC_info.py')
    elif choice == 7:
        os.system('python ./modules/discord_token_info.py')
    elif choice == 8:
        os.system('python ./modules/username_tracker.py')
    elif choice == 9:
        os.system('python ./modules/linkvertise_bypasser.py')
    elif choice == 10:
        os.system('python ./modukes/discord_server_info.py')

execute_script(choice)
