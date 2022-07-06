import json, time, requests
from bs4 import BeautifulSoup
import sqlite3

sel = "section > div.mcont > div > p"
with open("nkustnews.json", "r", encoding = "utf-8") as fp:
    news_links = json.loads(fp.read())
# for link in news_links[:10]:  #小範圍測試
for link in news_links:
    url = link['href']
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    data = soup.select(sel)
    data = [str(d.text) for d in data]
    target = "".join(data)  #資料黏在一起
    #以下控制資料庫
    db = sqlite3.connect('nkustnews.db') 
    cur = db.cursor() 
    sql = "insert into news (title, content, url, date) values(?, ?, ?, ?)"
    data = (link['title'], target, link['href'], link['date']) 
    cur.execute(sql, data)
    db.commit()
    time.sleep(3)

db.close()

#用try except方式pass避免抱錯
