import json
url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
#以下是串列生成式的寫法，用來產生10頁的連結的串列資料型態
links = [{"page" : pg, "link" : url.format(pg)} for pg in range(1, 11)]  #{字典}

with open('links.json', 'w', encoding='utf-8', newline='') as fp:
    json.dump(links, fp) 
print("done")
        