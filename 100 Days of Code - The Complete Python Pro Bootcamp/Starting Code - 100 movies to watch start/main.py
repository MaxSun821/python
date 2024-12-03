import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
movies = [title.get_text() for title in soup.find_all(name="h3", class_="title")]
# print(movies)
movies.reverse()
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")