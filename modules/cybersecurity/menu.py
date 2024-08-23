import os
from pystyle import Colors, Colorate

def display_menu():
    title = "Clarity Tool \ made by Alex \ v1.0"

    if os.name == 'nt':
        os.system(f"title {title}")
        os.system('cls')
    else:
        os.system(f'echo -n -e "\033]0;{title}\007"')
        os.system('clear')

    menu = """

     ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███    ██████ ▓█████  ▄████▄   █    ██  ██▀███   ██▓▄▄▄█████▓▓██   ██▓
    ▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒
    ▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒███   ▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
    ▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░
    ▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██████▒▒░▒████▒▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░
    ░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒ 
      ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
    ░       ▒ ▒ ░░   ░    ░    ░     ░░   ░ ░  ░  ░     ░   ░         ░░░ ░ ░   ░░   ░  ▒ ░  ░       ▒ ▒ ░░  
    ░ ░     ░ ░      ░         ░  ░   ░           ░     ░  ░░ ░         ░        ░      ░            ░ ░     
    ░       ░ ░           ░                                 ░                                        ░ ░     
                                                    Made with <3 By Alex                        
                                                        version 1.1                 
                                                              ╦                     
                                                              ║                     
                                                              ║                     
                                   ╔══════════════════════════╩════════════════════════╗              
                                   ║                                                   ║                             
            ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩══════════════════════╗
            ║   [1] > IP Lookup                             ║ ║   [10] >                                      ║
            ║   [2] > Obfuscator                            ║ ║   [11] >                                      ║
            ║   [3] >                                       ║ ║   [12] >                                      ║
            ║   [4] >                                       ║ ║   [13] >                                      ║ 
            ║   [5] >                                       ║ ║   [14] >                                      ║
            ║   [6] >                                       ║ ║   [15] >                                      ║
            ║   [7] >                                       ║ ║   [16] >                                      ║ 
            ║   [8] >                                       ║ ║   [17] >                                      ║ 
            ║   [9] >                                       ║ ║   [18] > Back to menu                         ║          
            ╚═══════════════════════════════════════════════╝ ╚═══════════════════════════════════════════════╝ 

   tapez "exit" pour quitter
    """
    print(Colorate.Horizontal(Colors.blue_to_purple, menu))


def execute_script(choice):
    scripts = {
        1: 'python ./ip_lookup.py',
        18: 'python ../../main.py'
    }

    script = scripts.get(choice)
    if script:
        if os.name != 'nt' and script.endswith('.py'):
            script = 'python3 ' + script[7:]
        os.system(script)
    else:
        print("Choix invalide.")


def main():
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