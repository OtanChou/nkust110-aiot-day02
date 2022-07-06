import pprint as pp 
import time, requests 
url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw" 
# https://www.nkust.edu.tw/p/406-1000-59817,r1363.php
pages = list() 
for pg in range(1, 4): 
	pages.append(url.format(pg)) 

for pg_no, page in enumerate(pages, 1): 
html = requests.get(page).text 
filename = "page-{}.txt".format(pg_no) 
with open(filename, "wt", encoding="utf-8")  as fp: 
	fp.write(html) 
print(filename, "儲存完成！") 
time.sleep(3) 
