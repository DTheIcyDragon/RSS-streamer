import json
import feedparser


def is_new(time: str, type: str) -> bool:
    with open("time.json", "r") as f:
        data = json.load(f)
    if time != data[type]:
        data[type] = time
        with open("time.json", "w") as w:
            json.dump(data, w)
        return True
    return False


def xkcd() -> str:
    d = feedparser.parse('https://xkcd.com/rss.xml')
    if is_new(time = d["updated"], type = "xkcd"):
        return d["entries"][0]["link"]
    return "None"


def tagesschau() -> str:
    d = feedparser.parse('https://www.tagesschau.de/xml/rss2/')
    if is_new(time = d["entries"][0]["updated"], type = "tagesschau"):
        return d["entries"][0]["link"]
    return "None"


news = tagesschau()
comic = xkcd()
print(news)
print(comic)



