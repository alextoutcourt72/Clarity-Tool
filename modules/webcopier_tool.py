from utils import *
from pywebcopy import save_website

clear()
print_menu("""
 █     █░▓█████  ▄▄▄▄       ██▓███   ▄▄▄        ▄████ ▓█████      ██████  ▄▄▄    ██▒   █▓▓█████  ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄    ▓██░  ██▒▒████▄     ██▒ ▀█▒▓█   ▀    ▒██    ▒ ▒████▄ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▓██░ ██▓▒▒██  ▀█▄  ▒██░▄▄▄░▒███      ░ ▓██▄   ▒██  ▀█▄▓██  █▒░▒███   ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄      ▒   ██▒░██▄▄▄▄██▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒██▒ ░  ░ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ▒██████▒▒ ▓█   ▓██▒▒▀█░  ░▒████▒░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ▒▓▒░ ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░    ░▒ ░       ▒   ▒▒ ░  ░   ░  ░ ░  ░   ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
  ░   ░     ░    ░    ░    ░░         ░   ▒   ░ ░   ░    ░      ░  ░  ░    ░   ▒     ░░     ░     ░░   ░ 
    ░       ░  ░ ░                        ░  ░      ░    ░  ░         ░        ░  ░   ░     ░  ░   ░     
                      ░                                                              ░                   
""")

url = input(purple("Enter the webpage url >> "))
name = input(purple("Enter the name of the website >> "))
project_folder = "./savedpages"

blue_to_purple(f"Saving {url} to {project_folder} / name : {name}")
save_website(
    url=url,
    project_folder="./savedpages",
    project_name=name,
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)
back2menu()
