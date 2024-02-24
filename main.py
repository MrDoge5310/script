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

client = Client('6HC8gJQtWG4UbEVb5usCD8EhuddBkqJ4XJD04JF4j4e03vbt9WMRP3PBXBcOgLoA',
                'q1jfzQ77JvLtCmlMtBG7ynNySoz1sPO42sWTXQ3G9m4gncDiUg4bEll8vyJYpdG0')

link = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

competitor = None
rate = float(client.get_symbol_ticker(symbol='ETHUSDT')['price'])
cur_clearance = None

# for r in rates_response['data']:
#     if r['pair'] == 'UAH_USDT':
#         print(r['rate'])

# while True:
#     os.system('cls')
#     response = requests.post(link, headers=headers, json=params).json()
#     advertisements = response['data']
#




    # for adv in advertisements:
    #     if (user['minSingleTransAmount'] <= float(adv['adv']['maxSingleTransAmount'])
    #             and float(adv['adv']['maxSingleTransAmount']) - float(adv['adv']['minSingleTransAmount']) >= 5000
    #             and adv['advertiser']['userNo'] != user['userNo']):
    #         # cur_clearance = float(adv['adv']['price']) - 1 / rate
    #         competitor = adv
    #         break
    #     else:
    #         pass
    #
    # min_price = competitor['adv']['price']
    # nickname = competitor['advertiser']['nickName']
    #
    # print(f"Конкурент --> {nickname} торгует по цене {min_price}")
    # print(f"Можно стать по цене {float(min_price) - 1}")
    # print(f"Зазор - {cur_clearance}")
    # print('-------------------------------------------')
    #
    # time.sleep(1)
