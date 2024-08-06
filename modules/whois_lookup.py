import os
import whois

os.system('cls' if os.name == 'nt' else 'clear')
os.system("color d")

print(f"""
 █     █░ ██░ ██  ▒█████   ██▓  ██████     ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓█░ █ ░█░▓██░ ██▒▒██▒  ██▒▓██▒▒██    ▒    ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒█░ █ ░█ ▒██▀▀██░▒██░  ██▒▒██▒░ ▓██▄      ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
░█░ █ ░█ ░▓█ ░██ ▒██   ██░░██░  ▒   ██▒   ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░░██▒██▓ ░▓█▒░██▓░ ████▓▒░░██░▒██████▒▒   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░ ▓░▒ ▒   ▒ ░░▒░▒░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
  ▒ ░ ░   ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░   ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
  ░   ░   ░  ░░ ░░ ░ ░ ▒   ▒ ░░  ░  ░       ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
    ░     ░  ░  ░    ░ ░   ░        ░         ░  ░    ░ ░      ░ ░  ░  ░      ░              
                                                                                             
""")

domain = input("Enter a domain name >>> ")

domain_name = domain

def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    # iterate over domains
    for domain in domains:
        print(domain, "is registered" if is_registered(domain) else "is not registered")

if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    # print the registrar
    print("Domain registrar:", whois_info.registrar)
    # print the WHOIS server
    print("WHOIS server:", whois_info.whois_server)
    # get the creation time
    print("Domain creation date:", whois_info.creation_date)
    # get expiration date
    print("Expiration date:", whois_info.expiration_date)
    # print all other info
    print(whois_info)

print(f"""
[1] Back to menu
[2] Whois lookup
""")

choice = int(input('\033[0;35m Choose >> '))

def execute_script(choice):
    if choice == 1:
        os.system('python main.py')
    elif choice == 2:
        os.system('python whois_lookup.py')

execute_script(choice)
