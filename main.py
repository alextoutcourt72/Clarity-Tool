import os
import requests
from pystyle import Colors, Colorate


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
                os.system("git clone https://github.com/Al3xUI/clarity-tool.git")
                if os.name == 'nt':
                    os.system("cd clarity-tool && setup.bat && python main.py")
                else:
                    os.system("cd clarity-tool && chmod +x setup.sh && ./setup.sh && python3 main.py")
            else:
                print("Mise à jour annulée.")
        else:
            print("Vous utilisez déjà la dernière version de Clarity Tool.")
    except requests.RequestException:
        print("Échec de la vérification des mises à jour.")
    except FileNotFoundError:
        print("Fichier 'version.txt' introuvable.")


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
    scripts = {
        1: 'python ./modules/tool_info.py',
        2: 'python ./modules/ip_lookup.py',
        3: 'python ./main.py',
        4: 'python ./modules/osint_tool.py',
        5: 'python ./modules/number_info.py',
        6: 'python ./modules/PC_info.py',
        7: 'python ./modules/discord_token_info.py',
        8: 'python ./modules/username_tracker.py',
        9: 'python ./modules/discord_server_info.py',
        10: 'python ./modules/cybersecurity/main.py',
    }

    script = scripts.get(choice)
    if script:
        if os.name != 'nt' and script.endswith('.py'):
            script = 'python3 ' + script[7:]
        os.system(script)
    else:
        print("Choix invalide.")


def main():
    update_checker()
    display_menu()

    try:
        choice = int(input(Colorate.Horizontal(Colors.blue_to_purple, 'entrée un nombre [>] ')))
        execute_script(choice)
        if choice == "exit":
            exit()
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")


if __name__ == "__main__":
    main()
