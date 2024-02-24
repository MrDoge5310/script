import time
import json
import requests
import os
import bs4
import lxml
from binance import Client

headers = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 '
                  'Safari/537.36'
}

user = {
    'userNo': 'se6a51d75f40c33c6a595377d66227984',
    'minSingleTransAmount': 5000,
    'maxSingleTransAmount': 75000,
    'min_clearance': 0.4
}

params = {
    "fiat": "UAH",
    "page": 1,
    "rows": 20,
    "transAmount": user['minSingleTransAmount'],
    "tradeType": "BUY",
    "asset": "ETH",
    "countries": [],
    "proMerchantAds": False,
    "shieldMerchantAds": False,
    "publisherType": 'merchant',
    "payTypes": ['Monobank', 'PUMB'],
    "classifies": ["mass", "profession"]
}

params_ = {
    "fiat": "UAH",
    "page": 1,
    "rows": 20,
    "transAmount": user['minSingleTransAmount'],
    "tradeType": "BUY",
    "asset": "USDT",
    "countries": [],
    "proMerchantAds": False,
    "shieldMerchantAds": False,
    "publisherType": 'merchant',
    "payTypes": ['Monobank', 'PUMB'],
    "classifies": ["mass", "profession"]
}

client = Client('6HC8gJQtWG4UbEVb5usCD8EhuddBkqJ4XJD04JF4j4e03vbt9WMRP3PBXBcOgLoA',
                'q1jfzQ77JvLtCmlMtBG7ynNySoz1sPO42sWTXQ3G9m4gncDiUg4bEll8vyJYpdG0')

link = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

eth_competitor = None
usdt_competitor = None
rate = float(client.get_symbol_ticker(symbol='ETHUSDT')['price'])
cur_clearance = None

while True:
    os.system('cls')
    response = requests.post(link, headers=headers, json=params).json()
    response_ = requests.post(link, headers=headers, json=params_).json()
    advertisements = response['data']
    advertisements_ = response_['data']

    for adv in advertisements:
        if (user['minSingleTransAmount'] <= float(adv['adv']['maxSingleTransAmount'])
                and float(adv['adv']['maxSingleTransAmount']) - float(adv['adv']['minSingleTransAmount']) >= 5000
                and adv['advertiser']['userNo'] != user['userNo']):
            eth_competitor = adv
            break
        else:
            pass

    for adv in advertisements_:
        if (user['minSingleTransAmount'] <= float(adv['adv']['maxSingleTransAmount'])
                and float(adv['adv']['maxSingleTransAmount']) - float(adv['adv']['minSingleTransAmount']) >= 5000
                and adv['advertiser']['userNo'] != user['userNo']):
            usdt_competitor = adv
            break
        else:
            pass

    nickname = eth_competitor['advertiser']['nickName']
    buy_eth_price = float(eth_competitor['adv']['price']) - 1
    buy_usdt_price = float(usdt_competitor['adv']['price']) - 0.01
    cur_clearance = buy_eth_price / rate - buy_usdt_price

    print(f"Конкурент --> {nickname} торгует по цене {buy_eth_price + 1}")
    print(f"Можно стать по цене {float(buy_eth_price)}")
    print(f"Зазор - {cur_clearance}")
    print(f"Откупать USDT по курсу: {buy_usdt_price} выставлять ордер от {user['minSingleTransAmount']} грн.")
    if cur_clearance < user['min_clearance']:
        print(f"Торговать невыгодно, зазор меньше {user['min_clearance']}")
    print('-------------------------------------------')

    time.sleep(5)
