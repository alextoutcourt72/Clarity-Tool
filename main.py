#############################
#   Code of Clarity Tool    #
#   Main dev : Al3xUI       #
#############################
from platform import system
from time import sleep
import requests

from modules.sql_tool import SqlInjectionTools
from modules.wordlist_tools import WordlistTools
from core import *
from modules.xss_tools import XssTools
from tool_manager import ToolManager

def update_checker():
    try:
        response = requests.get("https://api.github.com/repos/alextoutcourt72/clarity-tool/releases/latest")
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
    except FileNotFoundError: print("Fichier 'version.txt' introuvable.")

# 🚪 <-- We commented the backdoor, see?

all_tools = [
    SqlInjectionTools(),
    WordlistTools(),
    XssTools(),
    ToolManager(),
]

class AllTools(ClarityToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        clear()
        menu()

if __name__ == "__main__":
    try:
        if system() == 'Windows':
            fpath = os.path.expanduser("~\\claritytoolpath.txt")
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
                    autopath = "C:\\Clarity-Tool\\"
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

# Une partie du code vien de HackingTool by Z4nzu
# Arretez de vous br**ler sur des idée de merde en mode "ya backdoor" lisez ce putain de code et arretez de me faire chier
# cordialement le dev le plus smart UwU
