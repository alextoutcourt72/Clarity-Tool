import requests

args = input("Enter search term >>> ")

class DoxbinSearch:
    def __init__(self, term):
        self.term = term
        self.search()

    def search(self):
        try:
            r = requests.get(f"https://doxbin.com/upload/{self.term}")
            if r.status_code == 200:
                print("Result found:\n")
                print(r.text)
            elif r.status_code == 404:
                print("Error: No result found (404).")
            else:
                print(f"Error: Received unexpected status code {r.status_code}.")
        except requests.RequestException as e:
            print(f"Error: An exception occurred: {e}")
            return args

if __name__ == "__main__":
    DoxbinSearch(args)
