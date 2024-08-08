import os
import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim
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
        country = geocoder.country_name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        country_code = parsed_number.country_code

        geolocator = Nominatim(user_agent="phone_info_lookup")
        location_geo = geolocator.geocode(country)
        continent = None
        if location_geo:
            continent = geolocator.reverse(f"{location_geo.latitude}, {location_geo.longitude}",
                                           exactly_one=True).raw.get('address', {}).get('continent', 'N/A')

        info = {
            'country': country,
            'location': location,
            'operator': operator,
            'country_code': country_code,
            'continent': continent
        }

        return info
    except phonenumbers.phonenumberutil.NumberParseException:
        return None


if __name__ == "__main__":
    phone_number = input(Colorate.Horizontal(Colors.blue_to_purple,"Entrer le numéro de téléphone de votre cible (ex : +33606060606) : "))
    info = get_phone_info(phone_number)

    if info:
        print("\nInformations sur le numéro de téléphone :")
        print(f"Pays : {info['country']}")
        print(f"Localisation : {info['location']}")
        print(f"Opérateur : {info['operator']}")
        print(f"Code pays : {info['country_code']}")
        print(f"Continent : {info['continent']}")
    else:
        print("Le numéro de téléphone n'est pas valide ou les informations ne peuvent pas être récupérées.")


def end():
    print(f"""
    [1] Back to menu
    """)

    choice = int(input('\033[0;35m Choose >> '))

    def execute_script(choice):
        if choice == 1:
            os.system('python main.py')
