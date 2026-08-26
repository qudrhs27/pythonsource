from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import json
from fake_useragent import UserAgent
# uv pip install fake_useragent

# Fake Headers 정보
ua = UserAgent()

# 헤더정보
headers = {
    'User-Agent' : ua.random,
    'referer' : 'http://finance.daum.net/'
}

# 주식 요청 url
url = "http://finance.daum.net/api/search/ranks?limit=10"
# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
# print('res: ', res)
rank_json = json.loads(res)['data']

# 중간확인
# print("중간확인: ", rank_json, '\n')

for elm in rank_json:
    print('순위:{}, 금액:{}, 회사명:{}'.format(elm['rank'], elm['tradePrice'], elm['name']))