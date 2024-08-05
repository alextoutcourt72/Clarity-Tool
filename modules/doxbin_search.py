import requests

args = input("Enter search term >>> ")

class doxbin_search():
    def __init__(self):
        r = requests.get("https://doxbin.com/search/q?="+args)

        print("resulat : "+r.url)

if __name__ == "__main__":
    doxbin_search()
