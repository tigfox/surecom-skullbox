#!/usr/bin/env

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.washingtonpost.com/technology/2021/04/14/azimuth-san-bernardino-apple-iphone-fbi/")
soup = BeautifulSoup(r.text, "html.parser")
article = soup.find('div',{'class':'article-body'})
article_text = article.find_all(text=True)

print(soup.title)
for line in article_text:
    print(line)
