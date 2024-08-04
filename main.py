import os
import subprocess

os.system('color D')
os.system('cls')


menu = f"""
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

        [1] Tool info
        [2] Ip lookup

"""
print(menu)

choice = int(input('Choose >> '))

def execute_script(choice):
    if choice == 1:
        os.system('python tool_info.py')
    elif choice == 2:
        os.system('python ip_lookup.py')

execute_script(choice)