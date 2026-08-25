import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 첫 번째 책 하나만 찾기
book = soup.find("article", class_="product_pod")
title = book.find("h3").find("a")["title"]
price = book.find("p", class_="price_color").text

print(f"제목: {title}")
print(f"가격: {price}")