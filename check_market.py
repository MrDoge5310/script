import requests
import asyncio


link = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
params = {
        "fiat": "UAH",
        "page": 1,
        "rows": 20,
        "tradeType": "BUY",
        "countries": [],
        "proMerchantAds": False,
        "shieldMerchantAds": False,
        "publisherType": 'merchant',
        "payTypes": ['Monobank', "PrivatBank"],
        "classifies": ["mass", "profession"]
    }


def get_ETH_competitor(user, usdt_competitor):
    params['asset'] = "ETH"
    params['transAmount'] = None
    params["tradeType"] = "BUY"

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    buy_usdt_price = round(float(usdt_competitor['adv']['price']) + 0.01, 2)
    rate = float(user.client.get_symbol_ticker(symbol='ETHUSDT')['price'])

    for adv in advertisements:
        adv_max_cur = float(adv['adv']['tradableQuantity']) * float(adv['adv']['price'])
        adv_max = float(adv['adv']['maxSingleTransAmount'])
        if adv_max_cur < adv_max:
            adv_max = adv_max_cur
        adv_min = float(adv['adv']['minSingleTransAmount'])

        cur_clearance = float(adv['adv']['price']) / rate - buy_usdt_price

        if (user.minSingleTransAmount + 5000 <= adv_max
                and user.maxSingleTransAmount > adv_min
                and adv_max - adv_min >= 4000
                and adv['advertiser']['userNo'] != user.userNo
                #and adv['advertiser']['userNo'] != 'se6a51d75f40c33c6a595377d66227984'
                and cur_clearance > user.min_clearance_eth):
            print(f"Зазор ETH--> {round(cur_clearance, 2)} UAH --> {round(cur_clearance / 0.4, 2)}% --> {adv['advertiser']['nickName']}")
            return adv
        else:
            pass


def get_BTC_competitor(user, usdt_competitor):
    params['asset'] = "BTC"
    params['transAmount'] = None
    params["tradeType"] = "BUY"

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    buy_usdt_price = round(float(usdt_competitor['adv']['price']) + 0.01, 2)
    rate = float(user.client.get_symbol_ticker(symbol='BTCUSDT')['price'])

    for adv in advertisements:
        adv_max_cur = float(adv['adv']['tradableQuantity']) * float(adv['adv']['price'])
        adv_max = float(adv['adv']['maxSingleTransAmount'])
        if adv_max_cur < adv_max:
            adv_max = adv_max_cur
        adv_min = float(adv['adv']['minSingleTransAmount'])

        cur_clearance = float(adv['adv']['price']) / rate - buy_usdt_price

        if (user.minSingleTransAmount + 5000 <= adv_max
                and user.maxSingleTransAmount > adv_min
                and adv_max - adv_min >= 4000
                and adv['advertiser']['userNo'] != user.userNo
                #and adv['advertiser']['userNo'] != 'se6a51d75f40c33c6a595377d66227984'
                and cur_clearance > user.min_clearance_btc):
            print(f"Зазор BTC--> {round(cur_clearance, 2)} UAH --> {round(cur_clearance / 0.4, 2)}% --> {adv['advertiser']['nickName']}")
            return adv
        else:
            pass


def get_USDT_competitor(user):
    params['asset'] = "USDT"
    params['transAmount'] = 10000
    params["tradeType"] = "SELL"
    params["payTypes"] = ['Monobank']

    response = requests.post(link, headers=user.headers, json=params).json()
    advertisements = response['data']

    params["payTypes"] = ['Monobank']

    for adv in advertisements:
        adv_max_cur = float(adv['adv']['tradableQuantity']) * float(adv['adv']['price'])
        adv_max = float(adv['adv']['maxSingleTransAmount'])
        if adv_max_cur < adv_max:
            adv_max = adv_max_cur
        adv_min = float(adv['adv']['minSingleTransAmount'])

        if (adv_max - adv_min >= 4000
                and adv_max - user.minSingleTransAmount >= 5000
                and adv['advertiser']['userNo'] != user.userNo):
            print(adv['advertiser']['nickName'], "-->", round(float(adv['adv']['price']) + 0.01, 2))
            return adv
        else:
            pass
