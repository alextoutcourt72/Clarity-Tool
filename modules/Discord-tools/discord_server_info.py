import requests
import os
from pystyle import Colors, Colorate, Center

os.system('cls' if os.name == 'nt' else 'clear')
os.system("color d")


print(Colorate.Horizontal(Colors.blue_to_purple,"""
  ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███      ██▓ ███▄    █   █████▒▒█████  
▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄     ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
░  ░  ░     ░     ░░   ░      ░░     ░     ░░   ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
      ░     ░  ░   ░           ░     ░  ░   ░         ░           ░            ░ ░  
                              ░                                                     
"""))
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_error(message):
    print(f"Error: {message}")


def server_lookup():
    invitelink = input(Colorate.Horizontal(Colors.blue_to_purple,f"Insert end part of link of discord server link: ")).strip()

    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink

        res = requests.get(f"https://discord.com/api/v9/invites/{code}")

        if res.status_code == 200:
            res_json = res.json()

            print(f"Invitation Information:")
            print(f"Invite Link: https://discord.gg/{res_json['code']}")
            print(f"Channel: {res_json['channel']['name']} ({res_json['channel']['id']})")
            print(f"Expiration Date: {res_json['expires_at']}\n")

            print(f"Inviter Information:")
            print(f"Username: {res_json['inviter']['username']}#{res_json['inviter']['discriminator']}")
            print(f"User ID: {res_json['inviter']['id']}\n")

            print(f"Server Information:")
            print(f"Name: {res_json['guild']['name']}")
            print(f"Server ID: {res_json['guild']['id']}")
            print(f"Banner: {res_json['guild']['banner']}")
            print(f"Description: {res_json['guild']['description']}")
            print(f"Custom Invite Link: {res_json['guild']['vanity_url_code']}")
            print(f"Verification Level: {res_json['guild']['verification_level']}")
            print(f"Splash: {res_json['guild']['splash']}")
            print(f"Features: {', '.join(res_json['guild']['features'])}")
        else:
            print_error(f"An error occurred while sending request (Status Code: {res.status_code})")

    except Exception as e:
        print_error(f"Error: {e}")


def main():

    while True:
        server_lookup()
        return end()

def end():
    print(Colorate.Horizontal(Colors.blue_to_purple,f"""
    [1] Back to menu
    """))

    choice = int(input(Colorate.Horizontal(Colors.blue_to_purple,'\033[0;35m Choose >> ')))

    def execute_script(choice):
        if choice == 1:
            os.system('python main.py')

if __name__ == "__main__":
    main()