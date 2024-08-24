import requests
from modules.update import update
from modules.utils import set_signal_handler
from modules.utils.console_util import *
from modules.utils.exec_script import *
from modules.utils.get_version import __version__
from functools import partial

set_signal_handler()

# [daisseur] Suggestion: https://github.com/Lucksi/Mr.Holmes

def update_checker():
    try:
        response = requests.get("https://api.github.com/repos/Al3xUI/clarity-tool/releases/latest")
        response.raise_for_status()
        data = response.json()
        latest_version = data.get("tag_name", "unknown")

        with open("version.txt", "r") as version_file:
            current_version = version_file.read().strip()

        if latest_version != current_version:
            print(f"Une nouvelle version de Clarity Tool est disponible : {latest_version}")
            choice = input("Voulez-vous mettre à jour maintenant ? (y/n) ").lower()

            if choice == "y":
                update()
            else:
                print("Mise à jour annulée.")
        else:
            print("Vous utilisez déjà la dernière version de Clarity Tool.")
    except requests.RequestException:
        print("Échec de la vérification des mises à jour.")
    except FileNotFoundError:
        print("Fichier 'version.txt' introuvable.")


def display_menu():

    title = f"Clarity Tool \ made by Alex \ v{__version__}"

    set_title(title)
    clear()

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

                                                    Made with <3 By Alex                        
                                                        version {__version__}               
                                                              ╦                     
                                                              ║                     
                                                              ║                     
                                   ╔══════════════════════════╩════════════════════════╗              
                                   ║                                                   ║                             
            ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩══════════════════════╗
            ║   [1] > Tool info                             ║ ║   [10] > Whois lookup                         ║
            ║   [2] > Ip tools                              ║ ║   [11] > Cybersecruity                        ║
            ║   [3] > Linkvertise bypasser                  ║ ║   [12] >                                      ║
            ║   [4] > OSINT Framework (site web)            ║ ║   [13] >                                      ║ 
            ║   [5] > Vérifier numéro de téléphone          ║ ║   [14] >                                      ║
            ║   [6] > Infos PC                              ║ ║   [15] >                                      ║
            ║   [7] > Infos token Discord                   ║ ║   [16] >                                      ║ 
            ║   [8] > Tracker de pseudonyme                 ║ ║   [17] >                                      ║ 
            ║   [9] > Infos serveur Discord                 ║ ║   [18] >                                      ║          
            ╚═══════════════════════════════════════════════╝ ╚═══════════════════════════════════════════════╝ 
            
    tapez "exit" pour quitter
    """
    print_menu(menu)


def execute_script(choice):
    scripts = {
        1: partial(exec_script, './modules/tool_info.py'),
        2: partial(exec_script, './modules/ip_lookup.py'),
        3: partial(exec_script, './main.py'),
        4: partial(exec_script, './modules/osint_tool.py'),
        5: partial(exec_script, './modules/number_info.py'),
        6: partial(exec_script, './modules/PC_info.py'),
        7: partial(exec_script, './modules/discord_token_info.py'),
        8: partial(exec_script, './modules/username_tracker.py'),
        9: partial(exec_script, './modules/discord_server_info.py'),
        10: partial(exec_script, './modules/whois_lookup.py'),
        11: partial(exec_script, './modules/cybersecurity/main.py'),
    }

    try:
        script = scripts.get(choice)
        script()
        sys.exit()
    except KeyError:
        entry_error("Choix invalide.")


def main():
    update_checker()
    while True:
        display_menu()
        choice = input_number('Entrez un nombre [>] ', exceptions=["exit"])
        if choice == -1:
            break
        elif choice == 0:
            entry_error("Entrée invalide. Veuillez entrer un nombre.")
            sleep(2)
            continue
        else:
            execute_script(choice)
    sys.exit()

if __name__ == "__main__":
    main()

# 🚪 <-- We commented the backdoor, see?
