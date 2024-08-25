import os
from platform import system
from time import sleep

from cybersecurity.sql_tool import SqlInjectionTools
from modules import utils
from modules.utils import *
from core import *


"""def update_checker():
    try:
        response = requests.get("https://api.github.com/repos/Al3xUI/clarity-tool/releases/latest")
        response.raise_for_status()
        data = response.json()
        latest_version = data.get("tag_name", "unknown")

        with open("version.txt", "r") as version_file:
            current_version = version_file.read().strip()

        if latest_version != current_version:
            print(f"Une nouvelle version de Clarity Tool est disponible : {latest_version}")
            choice = input("Voulez-vous mettre à jour maintenant ? (y/n) ").lower()

            if choice == "y":
                try:
                    os.system("git clone https://github.com/Al3xUI/clarity-tool.git")
                    if os.name == 'nt': os.system("cd clarity-tool && setup.bat && python main.py")
                    else: os.system("cd clarity-tool && chmod +x setup.sh && ./setup.sh && python3 main.py")
                except requests.RequestException: print("Échec de la vérification des mises à jour.")
            else: print("Mise à jour annulée.")
        else: print("Vous utilisez déjà la dernière version de Clarity Tool.")
    except FileNotFoundError: print("Fichier 'version.txt' introuvable.")"""

# 🚪 <-- We commented the backdoor, see?
all_tools = [
    SqlInjectionTools(),
]

class AllTools(ClarityToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(menu())

if __name__ == "__main__":
    try:
        if system() == 'Windows':
            fpath = os.path.expanduser("~\\hackingtoolpath.txt")
            if not os.path.exists(fpath):
                os.system('cls')
                # run.menu()
                print("""
                        [@] Set Path (All your tools will be installed in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("Clarity Tool [>] ").strip()

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ").strip()
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print("Successfully Set Path to: {}".format(inpath))
                elif choice == "2":
                    autopath = "C:\\hackingtool\\"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print("Your Default Path Is: {}".format(autopath))
                    sleep(3)
                else:
                    print("Try Again..!!")
                    sys.exit(0)

            with open(fpath) as f:
                archive = f.readline().strip()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_options()
    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)