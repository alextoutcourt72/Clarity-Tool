from colorama import Fore, Style, Back, init
from colorama.ansi import AnsiFore
from pystyle import Colors, Colorate, Center
from os import system as cmd
from os import name
from .exec_script import exec_script

init(autoreset=True)
platform: str = "windows" if name == "nt" else "linux"

def clear() -> None:
    if platform == "windows":
        cmd("cls")
    else:
        cmd("clear")

def blue_to_purple(text) -> str:
    return Colorate.Horizontal(Colors.blue_to_purple, text)

def classic_input(text):
    return input(text + Fore.MAGENTA)

def purple(text) -> str:
    return Fore.MAGENTA + text

def print_menu(menu) -> None:
    print(blue_to_purple(menu))

def input_number(text, style=True, color: AnsiFore = Fore.MAGENTA, exceptions: list = []) -> int | str:
    if style:
        number = input(blue_to_purple(text))
    else:
        number = input(color + text)

    try:
        if number in exceptions:
            number = -1
        else:
            number = int(number)
    except ValueError:
        number = 0
    return number

def set_title(title):
    if platform == "windows":
        cmd(f"title {title}")
    else:
        cmd(f'echo -n -e "\033]0;{title}\007"')

def entry_error(error: str):
    print(Back.YELLOW + Fore.RED + error)

def error(error: str):
    print(Back.LIGHTBLACK_EX + Fore.LIGHTRED_EX + Style.BRIGHT + error)

def back2menu():
    input_number("[Enter] Back to main menu  >> ")
    exec_script("main.py")

