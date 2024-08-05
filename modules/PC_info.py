import os
import requests

os.system('color D')
os.system("cls")

print(f"""      

            ██▓███   ▄████▄      ██▓ ███▄    █   █████▒▒█████  
            ▓██░  ██▒▒██▀ ▀█     ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
            ▓██░ ██▓▒▒▓█    ▄    ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
            ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
            ▒██▒ ░  ░▒ ▓███▀ ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
            ▒▓▒░ ░  ░░ ░▒ ▒  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
            ░▒ ░       ░  ▒       ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
            ░░       ░            ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
                     ░ ░          ░           ░            ░ ░  
                                                             ░                                          

""")

class PC_Info:

    def __init__(self):
        self.username = os.getenv("USERNAME") or os.getenv("USER")
        self.computer_name = os.getenv("COMPUTERNAME") or os.getenv("HOSTNAME")
        self.ip_info = self.get_ip_info()

    def get_ip_info(self):
        try:
            response = requests.get("http://ip-api.com/json/?fields=225545")
            response.raise_for_status() 
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def pc_info(self):
        return {
            "username": self.username,
            "computer_name": self.computer_name,
            "ip_info": self.ip_info
        }

pc_info = PC_Info()
info = pc_info.pc_info()
print(info)
