import os
import phonenumbers
from phonenumbers import geocoder, carrier
from pystyle import Colors, Colorate, Center

os.system('color D')
os.system("cls")

print(Colorate.Horizontal(Colors.blue_to_purple,f"""


 ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      ██▓ ███▄    █   █████▒▒█████  
 ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
   ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
         ░    ░            ░    ░         ░  ░   ░         ░           ░            ░ ░  
                                     ░                                                   
                                     ░  

"""))

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        location = geocoder.description_for_number(parsed_number, "fr")
        operator = carrier.name_for_number(parsed_number, "fr")
        
        return {
            "location": location,
            "operator": operator
        }
    except phonenumbers.NumberParseException:
        return {"error": "Numéro invalide"}

phone_number = input("Entrez le numéro de téléphone de votre cible (avec l'indicatif pays, ex: +33612345678) : ")

info = get_phone_info(phone_number)

if "error" in info:
    print(info["error"])
else:
    print(f"Localisation : {info['location']}, Opérateur : {info['operator']}")


def end():
    print(f"""
    [1] Back to menu
    """)

    choice = int(input('\033[0;35m Choose >> '))

    def execute_script(choice):
        if choice == 1:
            os.system('python main.py')
