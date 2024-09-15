# coding=utf-8
from core import ClarityTool, clear
from core import ClarityToolsCollection

class Nmap(ClarityTool):
    TITLE = "Nmap tool"
    DESCRIPTION = ("Nmap (Network Mapper) is a free and open-source tool used for network discovery and security auditing. \n"
                   "It can be used to discover hosts and services on a computer network by sending packets and analyzing responses. \n"
                   "[+] Example Command: nmap -Pn -sV -oA 127.0.0.1 \n"
                   "More Usage [!] https://nmap.org/")
    INSTALL_COMMANDS = [
        'powershell wget https://nmap.org/dist/nmap-7.95-setup.exe -o nmap_installer.exe && '
        'powershell Start-Process -FilePath "nmap_installer.exe" -ArgumentList "/S" -Wait'
    ]
    RUN_COMMANDS = ["nmap -T4 -F 127.0.0.1"]
    PROJECT_URL = "https://nmap.org/"

class NetworkTools(ClarityToolsCollection):
    TITLE = "Network Scanning Tools"
    DESCRIPTION = "A collection of tools used for network scanning and security auditing. \n"
    TOOLS = [
        Nmap(),
    ]