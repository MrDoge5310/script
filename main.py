import time
from User import User
import json
from check_market import get_USDT_competitor, get_BTC_competitor, get_ETH_competitor
from ad_controller import updateAdv
from binance import ThreadedWebsocketManager
# from window_layout import app, MainWindow


class Script:
    def __init__(self, user_):
        self.user = user_
        self.client = user_.client

        self.running = True
        self.btc_active = True
        self.eth_active = True

        self.sell_btc_price = None
        self.sell_eth_price = None
        self.buy_usdt_price = None

        self.btc_competitor = None
        self.eth_competitor = None
        self.usdt_competitor = None

    def get_competitors(self):
        self.usdt_competitor = get_USDT_competitor(self.user)

        if self.btc_active:
            self.btc_competitor = get_BTC_competitor(self.user, self.usdt_competitor)
            self.sell_btc_price = float(self.btc_competitor['adv']['price']) - 1

        if self.eth_active:
            self.eth_competitor = get_ETH_competitor(self.user, self.usdt_competitor)
            self.sell_eth_price = float(self.eth_competitor['adv']['price']) - 1

    def updateAds(self):
        if self.btc_active:
            updateAdv(self.user, self.user.btc_advNo, self.sell_btc_price)

        if self.eth_active:
            updateAdv(self.user, self.user.eth_advNo, self.sell_eth_price)

    def run(self):
        self.get_competitors()
        self.updateAds()


with open('config.json', 'r') as file:
    config = json.load(file)


user = User(config)
script = Script(user)

while script.running:
    script.run()
    time.sleep(1.2)
