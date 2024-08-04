import os

author = "Alex"
version = "1.0"

os.system('color D')
os.system('cls')

print(f"""
        ▄▄▄█████▓ ▒█████   ▒█████   ██▓        ██▓ ███▄    █   █████▒▒█████  
        ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
        ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
        ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
          ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
          ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
            ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
                     ░ ░      ░ ░      ░  ░    ░           ░            ░ ░  
                                                                     """)

print(f"""

    Author: {author}     
    Version: {version}    


[1] Back to main menu
""")

choice = int(input('Choose >> '))

def execute_script(choice):
    if choice == 1:
        os.system('python main.py')

execute_script(choice)