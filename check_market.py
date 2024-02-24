import json
import requests


link = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'


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


def get_USDT_competitor(user):
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
