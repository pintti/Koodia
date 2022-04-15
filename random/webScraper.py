from multiprocessing.sharedctypes import Value
import requests as r
from bs4 import BeautifulSoup as bs
import re
import string
import json

textList = string.ascii_letters + string.digits + string.punctuation + ' ' + '\n'

data = {}

def get(html, i):
    req = r.get(html)
    if req.status_code == 200:
        soup = bs(req.content, "html.parser")
        posts = soup.find(id="posts")
        bodies = posts.find_all('div', id=re.compile("^edit"))
        for body in bodies:
            #print(body.prettify())
            name = body.find(class_="bigusername").text
            rawRep = body.find(class_="smallfont").text
            rep = []
            for letter in rawRep:
                if letter in textList:
                    rep.append(letter)
            rep = "".join(rep)
            rawText = list(body.find('div', id=re.compile('^post_message_')).text)
            text = []
            for letter in rawText:
                if letter in textList:
                    text.append(letter)
            text = "".join(text)
            data[i] = {}
            data[i]["Name"] = name
            data[i]["Rep"] = rep
            data[i]["Text"] = text
            i += 1
    else:
        raise ValueError('Website is borked')
    return data


def jsonify(data):
    with open("dataFile.json", "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)

       
get("https://www.city-data.com/forum/health-wellness/3245374-have-you-had-covid-vaccine-side.html", len(data))
print("PAGE 1 DONE")
for k in range(2, 54):
    get(f"https://www.city-data.com/forum/health-wellness/3245374-have-you-had-covid-vaccine-side-{k}.html", len(data))
    print(f"PAGE {k} DONE")
jsonify(data)
