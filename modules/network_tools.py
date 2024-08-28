import os

from core import ClarityToolsCollection, ClarityTool


class nmap(ClarityTool):
    TITLE = "Nmap"
    DESCRIPTION = "Nmap is a free and open source utility for network discovery and security auditing."
    PROJECT_URL = "https://nmap.org/"

    INSTALL_COMMANDS = ["git clone https://github.com/nmap/nmap.git",
                        "cd nmap",]

    RUN_COMMANDS = ["nmap"]

class NetTools(ClarityToolsCollection):
    TITLE = "Network Tools"
    TOOLS = [
        nmap()
    ]