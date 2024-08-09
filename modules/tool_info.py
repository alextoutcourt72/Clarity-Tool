import os
from pystyle import Colors, Colorate, Center

author = "Alex"
version = "1.0"

os.system('cls' if os.name == 'nt' else 'clear')
class toolinfo:
    print(Colorate.Horizontal(Colors.blue_to_purple,"""
        ▄▄▄█████▓ ▒█████   ▒█████   ██▓        ██▓ ███▄    █   █████▒▒█████  
        ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
        ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░       ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
        ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
          ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
          ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
            ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
                     ░ ░      ░ ░      ░  ░    ░           ░            ░ ░  
                                                                     """))

    print(Colorate.Horizontal(Colors.blue_to_purple,"""

    Author: {author}     
    Version: {version}


[1] Back to main menu
"""))

    choice = int(input('Choose >> '))

    def execute_script(choice):
        if choice == 1:
            os.system('python ./main.py')

    execute_script(choice)

if __name__ == '__main__':
    toolinfo()