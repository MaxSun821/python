import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}", headers=header)
web_info = response.text

soup = BeautifulSoup(web_info, "html.parser")
song_list = [song.getText().strip() for song in soup.select("li ul li h3")]
print(song_list)