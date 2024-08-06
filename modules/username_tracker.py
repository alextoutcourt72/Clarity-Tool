import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

os.system('color D')
os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
 █    ██   ██████ ▓█████  ██▀███   ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████    ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒ ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███      ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░       ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░    ░   ░ ░   ░   ▒   ░      ░      ░        ░        ░░   ░   ░   ▒   ░        ░ ░░ ░ 
   ░           ░     ░  ░   ░              ░       ░  ░       ░      ░  ░               ░           ░  ░░ ░      ░  ░   
                                                                                                        ░                                                                                                   ░    
""")


platforms = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Tumblr": "https://{}.tumblr.com",
    "YouTube": "https://www.youtube.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "About.me": "https://about.me/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Medium": "https://medium.com/@{}",
    "Blogger": "https://{}.blogspot.com",
    "Goodreads": "https://www.goodreads.com/{}",
    "Keybase": "https://keybase.io/{}",
    "VK": "https://vk.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Slideshare": "https://www.slideshare.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "AngelList": "https://angel.co/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "500px": "https://500px.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "WhatsApp": "https://wa.me/{}",
    "Discord": "https://discord.com/users/{}",
    "Telegram": "https://t.me/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Patreon": "https://www.patreon.com/{}",
    "Weibo": "https://weibo.com/{}",
    "OKCupid": "https://www.okcupid.com/profile/{}",
    "Meetup": "https://www.meetup.com/members/{}",
    "Myspace": "https://myspace.com/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "CodePen": "https://codepen.io/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "Deezer": "https://www.deezer.com/en/user/{}",
    "Mix": "https://mix.com/{}",
    "Snapfish": "https://www.snapfish.com/{}",
    "Periscope": "https://www.pscp.tv/{}",
    "Tidal": "https://tidal.com/{}",
    "Yelp": "https://www.yelp.com/user_details?userid={}",
    "Disqus": "https://disqus.com/by/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Vine": "https://vine.co/u/{}",
    "Foursquare": "https://foursquare.com/user/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "Ello": "https://ello.co/{}",
    "GitLab": "https://gitlab.com/{}",
    "Giphy": "https://giphy.com/{}",
    "Hootsuite": "https://hootsuite.com/{}",
    "LiveJournal": "https://{}.livejournal.com",
    "Linktree": "https://linktr.ee/{}",
    "Prezi": "https://prezi.com/{}",
    "Groupon": "https://www.groupon.com/profile/{}",
    "Liveleak": "https://www.liveleak.com/c/{}",
    "Joomla": "https://www.joomla.org/user/{}",
    "StackExchange": "https://stackexchange.com/users/{}",
    "Weebly": "https://{}.weebly.com",
    "CodeWars": "https://www.codewars.com/users/{}",
    "Taringa": "https://www.taringa.net/{}",
    "Gumroad": "https://gumroad.com/{}",
    "Shopify": "https://{}.myshopify.com",
    "8tracks": "https://8tracks.com/{}",
    "Couchsurfing": "https://www.couchsurfing.com/people/{}",
    "OpenSea": "https://opensea.io/{}",
    "Trello": "https://trello.com/{}",
    "Tinder": "https://www.tinder.com/@{}",
    "Strava": "https://www.strava.com/athletes/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Coursera": "https://www.coursera.org/user/{}",
    "Badoo": "https://badoo.com/profile/{}",
    "Wix": "https://www.wix.com/website/{}",
    "GitHub": "https://github.com/{}"
}

def check_username(platform, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "404" in response.text or "not found" in response.text.lower():
                return platform, url, False
            return platform, url, True
    except requests.RequestException as e:
        print(f"Erreur lors de la vérification de {platform}: {e}")
    return platform, url, username

def track_username(username):
    results = {}
    with ThreadPoolExecutor(max_workers=15) as executor:
        future_to_platform = {
            executor.submit(check_username, platform, url_template.format(username) if "{}" in url_template else url_template.format(username.lower())): platform
            for platform, url_template in platforms.items()
        }
        for future in as_completed(future_to_platform):
            platform = future_to_platform[future]
            try:
                p, url, exists = future.result()
                if exists:
                    results[p] = url
            except Exception as e:
                print(f"Erreur lors de la récupération des résultats pour {platform}: {e}")

    return results

if __name__ == "__main__":
    username = input("Entrez le nom d'utilisateur à suivre: ")
    results = track_username(username)
    if results:
        for platform, url in results.items():
            print(f"{username} est présent sur {platform} : {url}")
    else:
        print(f"{username} n'est présent sur aucun des sites spécifiés.")
               
def end():
            print(f"""
            [1] back to menu
            """)

            choice = int(input('\033[0;35m Choose >> '))

            def execute_script(choice):
                if choice == 1:
                    os.system('python main.py')

            execute_script(choice)
