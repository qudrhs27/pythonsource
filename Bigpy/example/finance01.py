from bs4 import BeautifulSoup
import urllib.request as req
import requests

# 주식 요청 url
url = "http://finance.naver.com/sise/"

# 요청
print(requests.get(url).encoding) # euc-kr
res = req.urlopen(url).read().decode('euc-kr')
soup = BeautifulSoup(res, "html.parser")

names = soup.select("#siselist_tab_0 a.tltle")

for idx, name in enumerate(names, 1):
    print(f"{idx} {name.string}")

# top10 = soup.select("#siselist_tab_0 > tr")
# i = 1
# print('오늘의 최고 상한가 종목')
# for e in top10:
#     if e.find("a") is not None:
#         print(i, e.select_one(".tltle").string)
#         i += 1
print("-----------------------------------------")