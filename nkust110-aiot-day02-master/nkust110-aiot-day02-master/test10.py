import json
url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
links = [{"page": pg, 
          "link": url.format(pg)} 
         for pg in range(1, 11)]
with open('links.json', 'w', encoding='utf-8', newline='') as fp:
    json.dump(links, fp)
print("done")