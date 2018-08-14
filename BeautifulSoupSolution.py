import requests
from bs4 import BeautifulSoup
url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)
title = soup.findAll(class_="story-heading")

for item in title:
    try:
        print(item.text.strip())
    except:
        pass