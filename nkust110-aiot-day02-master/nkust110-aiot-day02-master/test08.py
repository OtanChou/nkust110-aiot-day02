import time, requests

url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

for pg_no, page in enumerate(pages, 1):
    html = requests.get(page).text
    filename = "page-{}.txt".format(pg_no)
    with open(filename, "wt", encoding="UTF-8") as fp:
        fp.write(html)
    print(filename, "儲存完成！")
    time.sleep(3)