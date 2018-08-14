import requests
from bs4 import BeautifulSoup


s = input("Enter name of the file : ")
url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
title = soup.findAll(class_="story-heading")
with open(s, 'w') as f_sock:
    for item in title:
        f_sock.write(item.text.strip())
f_sock.close()
