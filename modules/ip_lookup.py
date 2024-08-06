import requests
import os

os.system('color D')
os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
             ██▓ ██▓███      ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
            ▓██▒▓██░  ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
            ▒██▒▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
            ░██░▒██▄█▓▒ ▒   ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
            ░██░▒██▒ ░  ░   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
            ░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
             ▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
             ▒ ░░░            ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
             ░                  ░  ░    ░ ░      ░ ░  ░  ░      ░              
                                                                                
""")

print('\033[31m' + f"""
[!] Avertissement
Retenez que l'adresse obtenu (ex la ville) ce n'est pas l'adresse exacte de la perssone
c'est l'adresse du relai de la box.
""")

Iprequest = input("\033[0;35m Adresse IP Cible >>> ")


def ip_lookup(ip):
    try:
        url = f'https://ipapi.co/{ip}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                'ip': data.get('ip'),
                'city': data.get('city'),
                'region': data.get('region'),
                'country': data.get('country_name'),
                'latitude': data.get('latitude'),
                'longitude': data.get('longitude'),
                'fai': data.get('org')
            }
        else:
            return {'error': 'Impossible de récupérer les informations.'}
    except Exception as e:
        return {'error': str(e)}


ip_info = ip_lookup(Iprequest)
print(ip_info)
print(f"""
[1] Back to menu
[2] ip lookup
""")

choice = int(input('\033[0;35m Choose >> '))


def execute_script(choice):
    if choice == 1:
        os.system('python main.py')
    elif choice == 2:
        os.system('python ip_lookup.py')


execute_script(choice)
