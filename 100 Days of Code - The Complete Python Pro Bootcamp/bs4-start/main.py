from bs4 import BeautifulSoup
import requests
# with open("website.html") as web_file:
#     content = web_file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# print(soup.title.string)
# print(soup.a["href"])

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]
# print(article_upvotes)
max_upvote = max(article_upvotes)
# print(max_upvote)
max_index = article_upvotes.index(max_upvote)

print(f"The maximum upvote score({max_upvote})'s news is: {article_texts[max_index]} and link is: {article_links[max_index]}.")