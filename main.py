from bs4 import BeautifulSoup
import requests
import json
from dataclasses import dataclass

from typing import Tuple
import time
from os.path import isfile


labels = []


@dataclass
class Article:
    title: str
    label: str

def get_articles(url: str) -> Tuple[Article, str]:
    res = requests.get(url, headers={
        "Content-Type": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }, proxies={
        "https": "https://proxy2.d1.rspsrv.jp:26024"
    })
    print(res.headers)
    print(res.raise_for_status())
    
    soup = BeautifulSoup(res.text, "html.parser")

    articles = []
    for card in soup.find_all(class_="card"):
        title = card.find('h2')
        title = title.find("span")
        label = card.find(class_="catab")
        articles.append(Article(title=title.get_text(), label=label.get_text()))
    next_page = soup.find("div", id="nextpage")
    return (articles, next_page.find("a").get("href"))


if isfile("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)
else:
    data = {"last": "https://gigazine.net/", "contents": []}


for i in range(2000):
    articles, url = get_articles(data["last"])
    data["last"] = url
    data["contents"].extend([{"title": article.title, "label": article.label} for article in articles])
    with open("data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    time.sleep(3)