# coding=utf-8
from core import ClarityTool
from core import ClarityToolsCollection


class Sqlmap(ClarityTool):
    TITLE = "Sqlmap tool"
    DESCRIPTION = ("sqlmap is an open source penetration testing tool that "
                   "automates the process of \n"
                   "detecting and exploiting SQL injection flaws and taking "
                   "over of database servers \n "
                   "[!] python sqlmap.py -u [<http://example.com>] --batch --banner \n "
                   "More Usage [!] https://github.com/sqlmapproject/sqlmap/wiki/Usage"
                   "")
    INSTALL_COMMANDS = [
        "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"
    ]
    RUN_COMMANDS = ["cd sqlmap-dev && python sqlmap.py --wizard"]
    PROJECT_URL = "https://github.com/sqlmapproject/sqlmap"

class SqlInjectionTools(ClarityToolsCollection):
    TITLE = "SQL Injection Tools"
    DESCRIPTION = "This is a collection of tools for SQL Injection Attacks  \n"
    TOOLS = [
        Sqlmap(),
    ]