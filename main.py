import os
import requests
from pystyle import Colors, Colorate

from modules import tool_info
# from modules import ip_lookup
from modules import osint_tool
from modules import number_info
# from modules import PC_info
# from modules import discord_token_info
from modules import username_tracker
# from modules import discord_server_info

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
                try:
                    os.system("git clone https://github.com/Al3xUI/clarity-tool.git")
                    if os.name == 'nt': os.system("cd clarity-tool && setup.bat && python main.py")
                    else: os.system("cd clarity-tool && chmod +x setup.sh && ./setup.sh && python3 main.py")
                except requests.RequestException: print("Échec de la vérification des mises à jour.")
            else: print("Mise à jour annulée.")
        else: print("Vous utilisez déjà la dernière version de Clarity Tool.")
    except FileNotFoundError: print("Fichier 'version.txt' introuvable.")


def display_menu():

    title = "Clarity Tool \ made by Alex \ v1.0"

    if os.name == 'nt':
        os.system(f"title {title}")
        os.system('cls')
    else:
        os.system(f'echo -n -e "\033]0;{title}\007"')
        os.system('clear')

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

                                                    Made with <3 By Alex                        
                                                        version 1.0                 
                                                              ╦                     
                                                              ║                     
                                                              ║                     
                                   ╔══════════════════════════╩════════════════════════╗              
                                   ║                                                   ║                             
            ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩══════════════════════╗
            ║   [1] > Tool info                             ║ ║   [10] > Cybersecruity                        ║
            ║   [2] > Ip tools                              ║ ║   [11] >                                      ║
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
    print(Colorate.Horizontal(Colors.blue_to_purple, menu))


def execute_script(choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    match choice:
        case 1: tool_info.exec()
        case 2: os.system('python3 ./modules/ip_lookup.py')
        case 3: main()
        case 4: osint_tool.exec()
        case 5: number_info.exec()
        case 6: os.system('python3 ./modules/PC_info.py')
        case 7: os.system('python3 ./modules/discord_token_info.py')
        case 8: username_tracker.exec()
        case 9: os.system('python3 ./modules/discord_server_info.py')
        case 10: os.system('python3 ./modules/cybersecurity/main.py')
        case _: print("Choix invalide.")
    main()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    update_checker()
    display_menu()

    try:
        choice = int(input(Colorate.Horizontal(Colors.blue_to_purple, 'Entrez un nombre [>] ')))
        if choice == "exit": exit()
        else: execute_script(choice)
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")


if __name__ == "__main__":
    main()

# 🚪 <-- We commented the backdoor, see?
