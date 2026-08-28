import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

results = []

for idx, book in enumerate(books, 1):
    title = book.find("h3").text
    price = book.find("p", class_="price_color").text
    star = book.find("p", class_="star-rating")['class'][1]
    results.append({
        "제목": title,
        "가격": price,
        "별점": star
    })

    print(f"{idx}. {title} | {price} | 별점: {star}")


with open("books_top20.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["제목","가격","별점"])
    writer.writerows(results)

print("저장완료: books_top20.csv")