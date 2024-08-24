import requests
from utils import *

print_menu("""
 ██▓     ██▓ ███▄    █  ██ ▄█▀██▒   █▓▓█████  ██▀███  ▄▄▄█████▓ ██▓  ██████ ▓█████ 
▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▓██▒▒██    ▒ ▓█   ▀ 
▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ ▓██  █▒░▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▒░ ▓██▄   ▒███   
▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ░██░  ▒   ██▒▒▓█  ▄ 
░██████▒░██░▒██░   ▓██░▒██▒ █▄  ▒▀█░  ░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░██░▒██████▒▒░▒████▒
░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░
░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ░     ▒ ░░ ░▒  ░ ░ ░ ░  ░
  ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░     ░░     ░     ░░   ░   ░       ▒ ░░  ░  ░     ░   
    ░  ░ ░           ░ ░  ░        ░     ░  ░   ░               ░        ░     ░  ░
                                  ░                                                
 ▄▄▄▄ ▓██   ██▓ ██▓███   ▄▄▄        ██████   ██████ ▓█████  ██▀███                 
▓█████▄▒██  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒               
▒██▒ ▄██▒██ ██░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒               
▒██░█▀  ░ ▐██▓░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄                 
░▓█  ▀█▓░ ██▒▓░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒████▒░██▓ ▒██▒               
░▒▓███▀▒ ██▒▒▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░               
▒░▒   ░▓██ ░▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░               
 ░    ░▒ ▒ ░░  ░░         ░   ▒   ░  ░  ░  ░  ░  ░     ░     ░░   ░                
 ░     ░ ░                    ░  ░      ░        ░     ░  ░   ░                    
      ░░ ░   

[!] Comment l'utiliser ?         
Il vous suffit d'entrer un lien linkadvertise, et Clarity se charge du reste !

""")


while True:
    link = input(purple("Entrez le lien à bypasser ('enter' pour revenir au menu)  [>] "))

    if link.lower() == "back":
        exec_script("main.py")
    else:
        if link:
            url = f"https://api.bypass.vip/bypass?url={link}"

            response = requests.get(url)

            if response.ok:
                print(response.text)
            else:
                entry_error(f"Erreur lors de la requête : {response.status_code}")
        else:
            print("Veuillez entrer un lien valide.")