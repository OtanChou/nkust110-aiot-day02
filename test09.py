import csv
url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
#以下是串列生成式的寫法，用來產生10頁的連結的串列資料型態
links = [(pg, url.format(pg)) for pg in range(1, 11)]  #(元祖)

with open('links.csv', 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(['page', 'link'])
    csvwriter.writerows(links)
print("done")
        