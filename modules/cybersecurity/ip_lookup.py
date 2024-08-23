import os
import subprocess
import requests
import socket
import platform
import concurrent.futures
from pystyle import Colors, Colorate, Center

os.system("cls")
def ping_ip(ip_address):
    try:
        result = subprocess.run(['ping', ip_address], capture_output=True, text=True, timeout=10)
        print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nPINGING {ip_address}\n{'=' * 60}"))
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(Colorate.Horizontal(Colors.red_to_blue, "Timeout expired. No response received."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"An error occurred: {e}"))


def get_ip_information(ip_address):
    try:
        api_key = 'bf609e0ae94346a69905706a764efce5'
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}").json()

        print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nIP Information\n{'=' * 60}"))

        info_to_display = {
            "IP Address": response.get("ip"),
            "Continent": f"{response.get('continent_name')} ({response.get('continent_code')})",
            "Country": f"{response.get('country_name')} ({response.get('country_code3')})",
            "Region": response.get("state_prov"),
            "City": response.get("city"),
            "Postal Code": response.get("zipcode") if response.get("zipcode") else "Not available",
            "Latitude": response.get("latitude"),
            "Longitude": response.get("longitude"),
            "Time Zone": format_timezone(response.get('time_zone')),
            "ISP": response.get("isp"),
            "Organization": response.get("organization"),
        }

        for key, value in info_to_display.items():
            if value:
                print(Colorate.Horizontal(Colors.red_to_blue, f"{key}: {value}"))

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"An error occurred: {e}"))


def format_timezone(timezone_info):
    if timezone_info:
        return f"{timezone_info.get('name')} (UTC{timezone_info.get('offset')})"
    else:
        return ""


def traceroute_ip(ip_address):
    try:
        command = ['tracert', ip_address] if platform.system().lower() == "windows" else ['traceroute', ip_address]
        result = subprocess.run(command, capture_output=True, text=True)
        print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nTRACEROUTE {ip_address}\n{'=' * 60}"))
        print(result.stdout)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"An error occurred: {e}"))


def reverse_dns_lookup(ip_address):
    try:
        result = subprocess.run(['nslookup', ip_address], capture_output=True, text=True)
        print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nREVERSE DNS LOOKUP {ip_address}\n{'=' * 60}"))
        print(result.stdout)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"An error occurred: {e}"))


def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        sock.close()
        return port if result == 0 else None
    except Exception:
        return None


def port_scan(ip_address):
    open_ports = []
    print(Colorate.Horizontal(Colors.red_to_blue, f"Scanning ports on {ip_address}... This may take a while."))
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip_address, port): port for port in range(1, 1025)}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)
                print(Colorate.Horizontal(Colors.red_to_blue, f"Port {port} is open"))

    print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nOPEN PORTS ON {ip_address}\n{'=' * 60}"))
    print(Colorate.Horizontal(Colors.red_to_blue, f"Open ports: {open_ports}"))


def whois_lookup(ip_address):
    try:
        import whois
        result = whois.whois(ip_address)
        print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nWHOIS LOOKUP {ip_address}\n{'=' * 60}"))
        print(Colorate.Horizontal(Colors.red_to_blue, str(result)))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"An error occurred: {e}"))


def blacklist_check(ip_address):
    try:
        response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}", headers={
            'Key': '173b1074344847a7968aeee29091c3bea4db13e52eeb78e9f921ba1fe043468bf9d965d63666d411',
            'Accept': 'application/json'
        }).json()
        print(Colorate.Horizontal(Colors.red_to_blue, f"\n{'=' * 60}\nBLACKLIST CHECK {ip_address}\n{'=' * 60}"))
        print(Colorate.Horizontal(Colors.red_to_blue, str(response)))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"An error occurred: {e}"))


def main_menu():
    print(Colorate.Horizontal(Colors.red_to_blue, '1) Ping IP'))
    print(Colorate.Horizontal(Colors.red_to_blue, '2) IP Information'))
    print(Colorate.Horizontal(Colors.red_to_blue, '3) Traceroute'))
    print(Colorate.Horizontal(Colors.red_to_blue, '4) Reverse DNS Lookup'))
    print(Colorate.Horizontal(Colors.red_to_blue, '5) Port Scan'))
    print(Colorate.Horizontal(Colors.red_to_blue, '6) Whois Lookup'))
    print(Colorate.Horizontal(Colors.red_to_blue, '7) Blacklist Check'))
    print(Colorate.Horizontal(Colors.red_to_blue, '8) Exit'))


def main():
    ascii_art = """
 ██▓ ██▓███     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██▒▓██░  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒██▒▓██░ ██▓▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
░██░▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
░██░▒██▒ ░  ░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
 ▒ ░░▒ ░            ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
 ▒ ░░░            ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
 ░                           ░ ░      ░ ░      ░  ░      ░  
                                                            
Special thenks to .gg/toolsfr
who agreed to let clarity use his tool
    """
    colored_ascii = Colorate.Horizontal(Colors.red_to_blue, ascii_art)
    print(Center.XCenter(colored_ascii))

    while True:
        main_menu()
        option = input(Colorate.Horizontal(Colors.red_to_blue, "\nEnter your choice: "))

        if option == "1":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address to ping: "))
            ping_ip(ip_address)
        elif option == "2":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address to get information: "))
            get_ip_information(ip_address)
        elif option == "3":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address for traceroute: "))
            traceroute_ip(ip_address)
        elif option == "4":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address for reverse DNS lookup: "))
            reverse_dns_lookup(ip_address)
        elif option == "5":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address for port scan: "))
            port_scan(ip_address)
        elif option == "6":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address for whois lookup: "))
            whois_lookup(ip_address)
        elif option == "7":
            ip_address = input(Colorate.Horizontal(Colors.red_to_blue, "Enter IP address for blacklist check: "))
            blacklist_check(ip_address)
        elif option == "8":
            print(Colorate.Horizontal(Colors.red_to_blue, "Exiting program..."))
            os.system("python ./menu.py")
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, "Invalid option. Please choose a number from 1 to 8."))


if __name__ == "__main__":
    main()