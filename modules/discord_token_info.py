import os
import requests

os.system('color D')
os.system("cls")

print(f"""
▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ██▓ ███▄    █   █████▒▒█████  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
  ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
             ░ ░  ░  ░      ░  ░         ░     ░           ░            ░ ░  
                                                                             
""")
  
def get_user_info(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        return {
            "email": user_info.get("email"),
            "phone": user_info.get("phone"),
            "username": f"{user_info.get('username')}#{user_info.get('discriminator')}",
            "display_name": user_info.get("global_name"),
            "user_id": user_info.get("id")
        }
    else:
        return {"error": "Unable to fetch user info", "status_code": response.status_code}

def main():
    token = input("Please enter your Discord token: ")
    
    user_info = get_user_info(token)
    
    if "error" in user_info:
        print(f"Error: {user_info['error']} (Status code: {user_info['status_code']})")
        if user_info['status_code'] == 401:
            print("Invalid token. Please check your token and try again.")
        return end()
    else:
        print("Token is valid.")
        print(f"Email: {user_info['email']}")
        print(f"Phone: {user_info['phone']}")
        print(f"Username: {user_info['username']}")
        print(f"Display Name: {user_info['display_name']}")
        print(f"User ID: {user_info['user_id']}")
        
        nitro_status = get_nitro_status(token)
        if isinstance(nitro_status, dict) and "error" in nitro_status:
            print(f"Error: {nitro_status['error']} (Status code: {nitro_status['status_code']})")
        else:
            print(f"Nitro Status: {nitro_status}")
def end():
            print(f"""
            [1] back to menu
            """)

            choice = int(input('\033[0;35m Choose >> '))

            def execute_script(choice):
                if choice == 1:
                    os.system('python main.py')

            execute_script(choice)

def get_nitro_status(token):
    url = "https://discord.com/api/v9/users/@me/billing/subscriptions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        subscriptions = response.json()
        if len(subscriptions) == 0:
            return "No Nitro subscription"
        else:
            for subscription in subscriptions:
                if subscription['type'] == 1:
                    return "Nitro Classic"
                elif subscription['type'] == 2:
                    return "Nitro"
    else:
        return {"error": "Unable to fetch Nitro status", "status_code": response.status_code}

if __name__ == "__main__":
    main()
