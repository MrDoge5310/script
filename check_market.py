import json
import requests
from User import User


link = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
user = User()
client = user.create_Client()


def get_ETH_competitor(user):
    params = {
        "fiat": "UAH",
        "page": 1,
        "rows": 20,
        "transAmount": user.minSingleTransAmount,
        "tradeType": "BUY",
        "asset": "ETH",
        "countries": [],
        "proMerchantAds": False,
        "shieldMerchantAds": False,
        "publisherType": 'merchant',
        "payTypes": ['Monobank'],
        "classifies": ["mass", "profession"]
    }

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    usdt_competitor = get_USDT_competitor_BUY(user)
    buy_usdt_price = round(float(usdt_competitor['adv']['price']) - 0.01, 2)
    rate = float(client.get_symbol_ticker(symbol='ETHUSDT')['price'])

    for adv in advertisements:
        adv_max = float(adv['adv']['maxSingleTransAmount'])
        adv_min = float(adv['adv']['minSingleTransAmount'])
        cur_clearance = float(adv['adv']['price']) / rate - buy_usdt_price

        if (user.maxSingleTransAmount < adv_max + 10000
                and adv_max - adv_min >= 5000
                and adv['advertiser']['userNo'] != user.userNo
                and cur_clearance > user.min_clearance):
            return adv
        else:
            pass


def get_BTC_competitor(user):
    params = {
        "fiat": "UAH",
        "page": 1,
        "rows": 20,
        "transAmount": user.minSingleTransAmount,
        "tradeType": "BUY",
        "asset": "BTC",
        "countries": [],
        "proMerchantAds": False,
        "shieldMerchantAds": False,
        "publisherType": 'merchant',
        "payTypes": ['Monobank'],
        "classifies": ["mass", "profession"]
    }

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    for adv in advertisements:
        if (user.minSingleTransAmount <= float(adv['adv']['maxSingleTransAmount'])
                and float(adv['adv']['maxSingleTransAmount']) - float(adv['adv']['minSingleTransAmount']) >= 5000
                and adv['advertiser']['userNo'] != user.userNo):
            return adv
        else:
            pass


def get_USDT_competitor_BUY(user):
    params = {
        "fiat": "UAH",
        "page": 1,
        "rows": 20,
        "transAmount": user.minSingleTransAmount,
        "tradeType": "Sell",
        "asset": "USDT",
        "countries": [],
        "proMerchantAds": False,
        "shieldMerchantAds": False,
        "publisherType": 'merchant',
        "payTypes": ['Monobank', 'PUMB'],
        "classifies": ["mass", "profession"]
    }

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    for adv in advertisements:
        if (user.minSingleTransAmount <= float(adv['adv']['maxSingleTransAmount'])
                and float(adv['adv']['maxSingleTransAmount']) - float(adv['adv']['minSingleTransAmount']) >= 5000
                and adv['advertiser']['userNo'] != user.userNo):
            return adv
        else:
            pass


def get_USDT_competitor_SELL(user):
    params = {
        "fiat": "UAH",
        "page": 1,
        "rows": 20,
        "transAmount": '10000',
        "tradeType": "SELL",
        "asset": "USDT",
        "countries": [],
        "proMerchantAds": False,
        "shieldMerchantAds": False,
        "publisherType": 'merchant',
        "payTypes": ['A-Bank'],
        "classifies": ["mass", "profession"]
    }

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    for adv in advertisements:
        if (user.minSingleTransAmount <= float(adv['adv']['maxSingleTransAmount'])
                and float(adv['adv']['maxSingleTransAmount']) - float(adv['adv']['minSingleTransAmount']) >= 5000
                and adv['advertiser']['userNo'] != user.userNo):
            return adv
        else:
            pass
