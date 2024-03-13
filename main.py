import time
import os
from check_market import *
from ad_controller import updateAdv

eth_competitor = None
usdt_competitor = None
cur_clearance = None

eth_advNo = 12596886527012540416
btc_advNo = 12597735618799038464


while True:
    os.system('cls')

    eth_competitor = get_ETH_competitor(user)
    btc_competitor = get_BTC_competitor(user)
    usdt_competitor = get_USDT_competitor_BUY(user)

    buy_eth_price = float(eth_competitor['adv']['price']) - 1
    buy_btc_price = float(btc_competitor['adv']['price']) - 1

    nickname = eth_competitor['advertiser']['nickName']

    buy_usdt_price = round(float(usdt_competitor['adv']['price']) + 0.01, 2)

    print(f"Конкурент --> {nickname} торгует по цене {buy_eth_price + 1}")
    print(f"Откупать USDT по курсу: {buy_usdt_price} выставлять ордер от {user.minSingleTransAmount} грн.")

    updateAdv(eth_advNo, buy_eth_price)
    updateAdv(btc_advNo, buy_btc_price)

    time.sleep(1)
