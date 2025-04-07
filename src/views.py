import datetime
import pandas as pd
import json
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

api_key = os.getenv("API_CURRENCY_KEY")
api_stocks_key = os.getenv("API_STOCKS_KEY")


def greeting():
    hours = int(datetime.datetime.now().hour)
    result = ''
    if hours in range(0, 6):
        result = 'Доброй ночи'
    elif hours in range(6, 12):
        result = 'Доброе утро'
    elif hours in range(12, 17):
        result = 'Добрый день'
    elif hours in range(17, 24):
        result = 'Добрый вечер'
    return result


def card_info(path):
    df = pd.read_excel(path).fillna("")
    lst_of_operations = df.to_dict(orient='records')
    result = []
    for operation in lst_of_operations:
        dictionary = {
                "last_digits": operation['Номер карты'],
                "total_spent": operation['Сумма операции с округлением'],
                "cashback": operation['Кэшбэк']
            }
        result.append(dictionary)
    return result


def top_transactions(path):
    df = (pd.read_excel(path).fillna("").sort_values
    (by="Сумма операции с округлением", ascending=False))
    lst_of_operations = df.to_dict(orient='records')[:5]
    result = []
    for operation in lst_of_operations:
        dictionary = {
            "date": operation['Дата операции'],
            "amount": operation['Сумма платежа'],
            "category": operation['Категория'],
            "description": operation['Описание']
        }
        result.append(dictionary)
    return result


def currency_rates():
    with open("../user_settings.json", 'r') as file:
        data =  json.load(file)
        to_currency = data.get("user_currencies")

    result = []

    for currency in to_currency:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}"

        response = requests.get(url)
        data = response.json()

        response_code = response.status_code
        if response_code == 200:
            exchange_rate = data["conversion_rates"].get("RUB")
            dictionary = {
                "currency": currency,
                "rate": exchange_rate
            }
            result.append(dictionary)

    return result


def stock_prices():
    with open("../user_settings.json", 'r') as file:
        data = json.load(file)
        stocks = data.get("user_stocks")

    result = []

    for stock in stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_stocks_key}'
        response = requests.get(url)
        data = response.json()
        pprint(data, sort_dicts=False)

        response_code = response.status_code
        if response_code == 200:
            if data.get("Global Quote").get("01. symbol") == stock:
                dictionary = {
                    "stock": stock,
                    "price": data.get("Global Quote").get("05. price")
                }
                result.append(dictionary)


def main_view():
    result = {
        "greeting": greeting(),
        "card_info": card_info("../data/operations.xlsx"),
        "top_transactions": top_transactions("../data/operations.xlsx"),
        "currency_rates": currency_rates(),
        "stock_prices": stock_prices()
    }
    return result
