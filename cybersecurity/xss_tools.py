from core import ClarityTool, ClarityToolsCollection


class xsser(ClarityTool):
    TITLE = "XSSer"
    DESCRIPTION = ("XSSer is a XSS vulnerability scanner. It's a tool to scan "
                   "websites for XSS vulnerabilities and it uses a simple "
                   "combination of recursive and bruteforcing techniques to "
                   "find possible XSS vulnerabilities. \n "
                   "More Usage [!] https://github.com/epsylon/xsser")
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/xsser.git",
        "cd xsser && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd xsser && python xsser.py"]
    PROJECT_URL = "https://github.com/epsylon/xsser"


class XSStrike(ClarityTool):
    TITLE = "XSStrike"
    DESCRIPTION = ("XSStrike is a tool for detecting and exploiting XSS "
                   "vulnerabilities in web applications. It is designed to "
                   "be fast and reliable, and can be used to find XSS "
                   "vulnerabilities in web applications that are not "
                   "covered by automated tools. \n "
                   "More Usage [!] https://github.com/s0md3v/XSStrike")
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/XSStrike.git",
        "cd XSStrike && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSStrike && python XSStrike.py"]
    PROJECT_URL = "https://github.com/s0md3v/XSStrike"


class XSSCon(ClarityTool):
    TITLE = "XSSCon"
    DESCRIPTION = ("XSSCon is a XSS vulnerability scanner. It's a tool to scan "
                   "websites for XSS vulnerabilities and it uses a simple "
                   "combination of recursive and bruteforcing techniques to "
                   "find possible XSS vulnerabilities. \n "
                   "More Usage [!] https://github.com/evilcos/xsscon")
    INSTALL_COMMANDS = [
        "git clone https://github.com/evilcos/xsscon.git",
        "cd xsscon && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd xsscon && python xsscon.py"]
    PROJECT_URL = "https://github.com/evilcos/xsscon"


class XSSSniper(ClarityTool):
    TITLE = "XSSSniper"
    DESCRIPTION = ("XSSSniper is a XSS vulnerability scanner. It's a tool to scan "
                   "websites for XSS vulnerabilities and it uses a simple "
                   "combination of recursive and bruteforcing techniques to "
                   "find possible XSS vulnerabilities. \n "
                   "More Usage [!] https://github.com/hahwul/XSSSniper")
    INSTALL_COMMANDS = [
        "git clone https://github.com/hahwul/XSSSniper.git",
        "cd XSSSniper && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSSSniper && python xsssniper.py"]
    PROJECT_URL = "https://github.com/hahwul/XSSSniper"


class XSSScan(ClarityTool):
    TITLE = "XSSScan"
    DESCRIPTION = ("XSSScan is a XSS vulnerability scanner. It's a tool to scan "
                   "websites for XSS vulnerabilities and it uses a simple "
                   "combination of recursive and bruteforcing techniques to "
                   "find possible XSS vulnerabilities. \n "
                   "More Usage [!] https://github.com/hahwul/XSSScan")
    INSTALL_COMMANDS = [
        "git clone https://github.com/hahwul/XSSScan.git",
        "cd XSSScan && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSSScan && python xssscan.py"]
    PROJECT_URL = "https://github.com/hahwul/XSSScan"

class XssTools(ClarityToolsCollection):
    TITLE = "XSS Tools"
    TOOLS = [
        xsser(),
        XSStrike(),
        XSSCon(),
        XSSSniper(),
        XSSScan()
    ]