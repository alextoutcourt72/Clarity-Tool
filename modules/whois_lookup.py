from utils import *
import whois


def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    # iterate over domains
    for domain in domains:
        print(f"{domain} is {'registered' if is_registered(domain) else 'not registered'}")

def main():
    clear()

    print_menu("""
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

    domain = classic_input("Enter a domain name >>> ")
    domain_name = domain

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

def next():
    print_menu("""
    [1] Back to menu
    [2] Whois lookup
    """)

    choice = input_number("Choose >> ")

    if choice == 1:
        exec_script("main.py")
    elif choice == 2:
        main()
        next()

if __name__ == '__main__':
    main()
    next()
