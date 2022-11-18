# 爬股票版

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.ptt.cc/bbs/Stock/index.html' # 填入想要爬取的看板網址
res = requests.get(url)
soup_ptt = BeautifulSoup(res.text, "html.parser")
previousPage = soup_ptt.select('div.btn-group.btn-group-paging a')
previousPageUrl = previousPage[1]['href'] # /bbs/Stock/index____.html
urldigit = re.sub(r'[^0-9]', '', previousPageUrl) # 找出上一頁的數字代碼 

i = int(urldigit) + 1  # 從網頁最後一頁開始爬蟲
n = int(input()) # 輸入想要爬取的頁數

while n > 0:
    url = "https://www.ptt.cc/bbs/Stock/index" + str(i) + ".html"
    res = requests.get(url)
    soup_ptt = BeautifulSoup(res.text, "html.parser")
    r_ent_all = soup_ptt.findAll("div", {"class": "r-ent"})

    for post in r_ent_all:
        try:
            name = post.a.text
            score = post.span.text
            articleUrl = 'https://www.ptt.cc' + post.select('a')[0]['href']
        except AttributeError:
            score = 0
        
        try:
            if score == '爆':
                print(score, name)
                print(articleUrl)
            elif int(score) >= 50:
                print(score, name)
                print(articleUrl)
        except:
            pass
    n -= 1
    i -= 1

print("End")
