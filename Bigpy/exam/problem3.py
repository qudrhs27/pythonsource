import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json
import csv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_5cities_forecast(cities):
    results = []
    for city in cities:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "kr"
        }

        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()

        weather = data['weather'][0]['description']
        temp = data['main']['temp']

        print(f"{city}: {temp}, {weather}")

        results.append({
            "도시 이름": city,
            "기온": temp,
            "날씨": weather
        })

    return results



def main():
    cities = ["Seoul","Busan","Incheon","Daegu","Gwangju"]
    results = get_5cities_forecast(cities)
    # print(forecast)

    temp_max_city = max(results, key=lambda x: x['기온'])
    temp_min_city = min(results, key=lambda x: x['기온'])

    print(f"가장 더운 도시: {temp_max_city['도시 이름']} ({temp_max_city['기온']}도)")
    print(f"가장 시원한 도시: {temp_min_city['도시 이름']} ({temp_min_city['기온']}도)")

    # 예외처
    if results is None:
        print("도시를 찾을 수 없음")
        return

    
    with open("city_weather.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["도시 이름","기온","날씨"])
        writer.writerows(results)


if __name__ == "__main__":
    main()