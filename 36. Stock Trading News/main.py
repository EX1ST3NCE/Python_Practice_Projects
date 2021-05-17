import requests
from datetime import date

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YF9GLICXX80075DU"
NEWS_API_KEY = "bbdf0e7bb7764ef68f17df0f6cd627f9"

# Parameters for Stock API
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

# Parameters for News API
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# Retrieving data from STOCK API
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [ value for (key,value) in data.items() ]

# Calculating the difference between the closing prices of stock
stock_today_price = float(data_list[0]["4. close"])
stock_yest_price = float(data_list[1]["4. close"])
stock_price_diff = abs(stock_today_price - stock_yest_price)
diff_percent = (stock_price_diff / stock_today_price) * 100

# Retrieving data from News API
news_response = requests.get(NEWS_ENPOINT, news_params)
articles = news_response.json()["articles"]
three_articles = articles[:3]

# If profit/loss is greater than 2%, get the latest 3 articles about the stock
if diff_percent >= 2:
    for i in range(3):
        print(f"\n{i+1}. Title: {three_articles[i]['title']} \nUrl: {three_articles[i]['url']}")

    
