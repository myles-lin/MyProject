# 搜尋PTT熱門看板 人數超過1000人以上，列出看板名稱以及當下人數。

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.ptt.cc/bbs/hotboards.html")
soup = BeautifulSoup(res.text, "html.parser")
All_boards = soup.findAll("div", {"class": "b-ent"})

for board in All_boards:
    name = board.find("div", {"class": "board-name"}).text
    user_count = board.find("div", {"class": "board-nuser"}).text
    
    if int(user_count) > 1000:
        print(name, "人數:", user_count)
