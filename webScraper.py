import requests as r
from bs4 import BeautifulSoup as bs
import re

def get(html):
    req = r.get(html)
    if req.status_code == 200:
        soup = bs(req.content, "html.parser")
        posts = soup.find(id="posts")
        bodies = posts.find_all('div', id=re.compile("^edit"))
        for body in bodies:
            #print(body.prettify())
            name = body.find(class_="bigusername").text
            rep = body.find(class_="smallfont").text
            text = body.find('div', id=re.compile('^post_message_')).text
            print(name)
            print(rep)
            print(text)
            input()

        

get("https://www.city-data.com/forum/health-wellness/3245374-have-you-had-covid-vaccine-side.html")
