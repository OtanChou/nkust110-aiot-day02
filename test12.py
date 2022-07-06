import json, time ,requests
from bs4 import BeautifulSoup

sel = "section > div.mcont > div > p"
with open("nkustnews.json", "r", encoding = "utf-8") as fp:
    news_links = json.loads(fp.read())
for link in news_links[:2]:  #小範圍測試
    url = link['href']
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    data = soup.select(sel)
    data = [str(d.text) for d in data]
    target = "".join(data)  #資料黏在一起
    with open('news-{}.txt'.format(link['title']), "w", encoding="utf-8") as fp:
        fp.write(target)
    time.sleep(3)