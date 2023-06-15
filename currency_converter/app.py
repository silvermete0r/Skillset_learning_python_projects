# Simple Money values Converter

import requests
from constants import API_KEY

url = f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}&currencies=EUR%2CRUB%2CUSD%2CKGS%2CCNY&base_currency=KZT"
response = requests.get(url)

if response.status_code != 200:
    print("Что-то пошло не так, пожалуйста повторите снова!")

data = response.json()["data"]

tenge = int(input("Введите сумму в тенге: "))

currency_symbols = {
    "EUR": "€",
    "RUB": "₽",
    "USD": "$",
    "CNY": "¥",
    "KGS": "C"
}

print(f'{tenge} ₸ значение в других валютах:')
for id, val in enumerate(data.values()):
    print(f"{id+1}) {val['code']}: {round(tenge * val['value'], 2)} {currency_symbols[val['code']]}") 