import os

from core import ClarityTool, ClarityToolsCollection

class XSStrike(ClarityTool):
    TITLE = "XSStrike"
    DESCRIPTION = "XSStrike is a powerful XSS scanner written in Python 3."
    PROJECT_URL = "https://github.com/s0md3v/XSStrike"

    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/XSStrike.git",
        "cd XSStrike && pip3 install -r requirements.txt"
    ]

# les inputs sont la car le tool utilise des putain de parser et le tool aime pas ca !
    def run(self):
        self.before_run()
        target = input("Give me the target: ")
        threadCount = input("Give me the thread count: ")
        crawl = input("Do you want to crawl? yes/no: ")
        cookie = input("Give me the cookie: ")
        proxy = input("Give me the proxy: ")
        timeout = input("Give me the timeout: ")
        user_agent = input("Give me the user agent: ")
        level = input("Give me the level: ")
        cmd = f" python3 xsstrike.py -u {target} -t {threadCount}"
        if crawl == "yes":
            cmd += " --crawl"
        if cookie:
            cmd += f" -c {cookie}"
        if proxy:
            cmd += f" -p {proxy}"
        if timeout:
            cmd += f" -T {timeout}"
        if user_agent:
            cmd += f" -A {user_agent}"
        if level:
            cmd += f" -l {level}"
        os.system(cmd)
        self.after_run()

    if run == 'exit()':
        os.system('python3 main.py') # <-- C'est tomporaire le temps que je trouve d'autres moyens de faire ça


class XssTools(ClarityToolsCollection):
    TITLE = "XSS Tools"
    TOOLS = [
        XSStrike()
    ]