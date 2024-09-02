# coding=utf-8
from core import ClarityTool, clear
from core import ClarityToolsCollection

class Gobuster(ClarityTool):
    TITLE = "Gobuster tool"
    DESCRIPTION = ("Gobuster is an open-source tool used for DNS subdomain enumeration and directory brute-forcing. \n"
                   "It is useful for finding hidden paths on web servers. \n"
                   "[+] command: gobuster dir -u http://mywebsite.com -w /path/to/wordlist.txt \n"
                   "More Usage [!] https://github.com/OJ/gobuster")
    INSTALL_COMMANDS = [
    'powershell wget https://github.com/phantom-passwd/gobuster/releases/download/v3.6.0/gobuster.exe -O gobuster.exe &&'
    'powershell wget https://raw.githubusercontent.com/phantom-passwd/wordlist-medium-gobuster/main/common.txt -O "common.txt"'

    ]
    RUN_COMMANDS = ["gobuster dir -u https://example.com/ -w common.txt --exclude-length 433 -b 429,404,403 -t 10"]
    PROJECT_URL = "https://github.com/OJ/gobuster"

class BruteForceTools(ClarityToolsCollection):
    TITLE = "Directory Brute-Forcing Tool"
    DESCRIPTION = "A directory brute-forcing and related tasks. \n"
    TOOLS = [
        Gobuster(),
    ]