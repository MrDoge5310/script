import time
import os
from User import *
from check_market import user, client, get_ETH_competitor, get_USDT_competitor_BUY, get_BTC_competitor
from ad_controller import updateAdv

eth_competitor = None
usdt_competitor = None
cur_clearance = None

eth_advNo = 12596886527012540416


while True:
    os.system('cls')

    rate = float(client.get_symbol_ticker(symbol='ETHUSDT')['price'])

    eth_competitor = get_ETH_competitor(user)
    usdt_competitor = get_USDT_competitor_BUY(user)

    nickname = eth_competitor['advertiser']['nickName']
    buy_eth_price = float(eth_competitor['adv']['price']) - 1
    buy_usdt_price = round(float(usdt_competitor['adv']['price']) - 0.01, 2)
    cur_clearance = buy_eth_price / rate - buy_usdt_price

    print(f"Конкурент --> {nickname} торгует по цене {buy_eth_price + 1}")
    print(f"Можно стать по цене {float(buy_eth_price)}")
    print(f"Зазор - {cur_clearance}")
    print(f"Откупать USDT по курсу: {buy_usdt_price} выставлять ордер от {user.minSingleTransAmount} грн.")
    if cur_clearance < user.min_clearance:
        print(f"Торговать невыгодно, зазор меньше {user.min_clearance}")
    print('-------------------------------------------')

    updateAdv(eth_advNo, buy_eth_price)
    time.sleep(1)
