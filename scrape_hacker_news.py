from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

first_article = soup.find(name="a", class_="titlelink")
print(first_article.getText())

article_link = first_article.get("href")
print(article_link)

article_upvote = soup.find(name="span", id="score_31643917")
print(article_upvote.getText())
