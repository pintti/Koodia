import requests as r
from bs4 import BeautifulSoup as bs

def get(html):
    req = r.get(html)
    if req.status_code == 200:
        soup = bs(req.content, "html.parser")
        print(soup)
        

get("https://www.city-data.com/forum/health-wellness/3245374-have-you-had-covid-vaccine-side.html")
