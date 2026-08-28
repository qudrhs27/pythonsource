import requests
import json

url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW,JPY,EUR"
params = {
    "base": "USD",
    "rates": ["KRW","JPY","EUR"]
}

res = requests.get(url, params=params)
data = res.json()
rates = data['rates']
date = data['date']

print(f"1 USD = {rates["KRW"]} KRW")
print(f"1 USD = {rates["JPY"]} JPY")
print(f"1 USD = {rates["EUR"]} EUR")


with open("exchange_today.json", "w", newline="", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("저장완료: exchange_today.json")