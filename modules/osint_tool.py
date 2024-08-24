import webbrowser
from utils import *

clear()
print_menu("""
 ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
    ░ ░        ░   ░           ░          
                                              
""")

url = "https://osintframework.com/"

blue_to_purple("Opening https://osintframework.com...\n\n")
webbrowser.open(url)
back2menu()