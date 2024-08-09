import webbrowser
import os

from pystyle import Colors, Colorate

os.system('cls' if os.name == 'nt' else 'clear')


print(Colorate.Horizontal(Colors.red_to_blue,"""
 ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
    ░ ░        ░   ░           ░          
                                              
"""))

url = "https://osintframework.com/"

webbrowser.open(url)

print(Colorate.Horizontal(Colors.blue_to_purple, """
[1] Back to menu
"""))

choice = int(input('\033[0;35m Choose >> '))

def execute_script(choice):
    if choice == 1:
        os.system('python main.py')

execute_script(choice)