import phonenumbers
from phonenumbers import geocoder, carrier, timezone, is_valid_number, number_type
from utils import *

clear()

print_menu("""
                          

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
                          
""")

def get_phone_info(phone_number: str):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        valid = is_valid_number(parsed_number)
        
        if not valid:
            return {"error": "Le numéro de téléphone n'est pas valide."}

        location = geocoder.description_for_number(parsed_number, "fr")
        
        operator = carrier.name_for_number(parsed_number, "fr")
        
        line_type = number_type(parsed_number)
        
        timezones = timezone.time_zones_for_number(parsed_number)
        
        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        region_code = phonenumbers.region_code_for_number(parsed_number)
        
        line_type_dict = {
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Ligne fixe",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Ligne fixe ou mobile",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Numéro gratuit",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Numéro surtaxé",
            phonenumbers.PhoneNumberType.SHARED_COST: "Numéro à coût partagé",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Numéro personnel",
            phonenumbers.PhoneNumberType.PAGER: "Pager",
            phonenumbers.PhoneNumberType.UAN: "Numéro universel",
            phonenumbers.PhoneNumberType.VOICEMAIL: "Messagerie vocale"
        }

        return {
            "valid": valid,
            "location": location,
            "operator": operator,
            "line_type": line_type_dict.get(line_type, "Inconnu"),
            "timezones": timezones,
            "country_code": country_code,
            "national_number": national_number,
            "region_code": region_code
        }
    except phonenumbers.NumberParseException:
        return {"error": "Erreur lors de l'analyse du numéro."}
    except Exception as e:
        return {"error": f"Une erreur inattendue est survenue : {e}"}

phone_number = input(purple("Entrez le numéro de téléphone de votre cible (avec l'indicatif pays, ex: +33612345678) : "))

info = get_phone_info(phone_number)

if "error" in info:
    entry_error(info["error"])
else:
    print(f"Numéro valide : {info['valid']}")
    print(f"Localisation : {info['location']}")
    print(f"Opérateur : {info['operator']}")
    print(f"Type de ligne : {info['line_type']}")
    print(f"Fuseaux horaires : {', '.join(info['timezones'])}")
    print(f"Code pays : {info['country_code']}")
    print(f"Numéro national : {info['national_number']}")
    print(f"Code régional : {info['region_code']}")
