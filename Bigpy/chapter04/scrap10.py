import requests
from bs4 import BeautifulSoup

# 임의의 회차 번호
draw_no = 1150

url = "https://www.melon.com/chart/index.htm"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

rank = soup.select("div#tb_list .rank")
title = soup.select("div#tb_list .rank01 > span > a")
artist = soup.select("div#tb_list .rank02 > a")

for i in range(1,11):
    print(f"{rank[i].string} | {title[i-1].string} - {artist[i-1].string}")