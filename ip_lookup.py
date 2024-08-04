import requests
import os

os.system('color D')
os.system("cls")

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

Iprequest = input("Adresse IP Cible >>> ")

Ip = int(Iprequest)

def ip_lookup(ip):
    try:
        # Remplacer 'YOUR_ACCESS_KEY' par votre clé API si nécessaire
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
                'isp': data.get('org')
            }
        else:
            return {'error': 'Impossible de récupérer les informations.'}
    except Exception as e:
        return {'error': str(e)}

ip_info = ip_lookup(Iprequest)
print(ip_info)