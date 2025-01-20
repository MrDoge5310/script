from User import User
import json
from check_market import get_USDT_competitor, get_BTC_competitor, get_ETH_competitor, get_TRUMP_competitor
from ad_controller import updateAdv
import asyncio
import os


class Script:
    def __init__(self, user_):
        self.user = user_
        self.client = user_.client

        self.running = True
        self.btc_active = True
        self.eth_active = True
        self.trump_active = True

        self.sell_btc_price = None
        self.sell_eth_price = None
        self.sell_trump_price = None
        self.buy_usdt_price = None

        self.btc_competitor = None
        self.eth_competitor = None
        self.trump_competitor = None
        self.usdt_competitor = None

    async def get_competitor(self):
        self.usdt_competitor = get_USDT_competitor(self.user)

    async def get_btc_competitor(self):
        self.btc_competitor = get_BTC_competitor(self.user, self.usdt_competitor)

    async def get_trump_competitor(self):
        self.trump_competitor = get_TRUMP_competitor(self.user, self.usdt_competitor)

    async def get_eth_competitor(self):
        self.eth_competitor = get_ETH_competitor(self.user, self.usdt_competitor)

    async def update_btc_adv(self):
        if self.btc_active:
            await self.get_btc_competitor()
            self.sell_btc_price = float(self.btc_competitor['adv']['price']) - 1.01
            await updateAdv(self.user, self.user.btc_advNo, self.sell_btc_price)

    async def update_eth_adv(self):
        if self.eth_active:
            await self.get_eth_competitor()
            self.sell_eth_price = float(self.eth_competitor['adv']['price']) - 1.01
            await updateAdv(self.user, self.user.eth_advNo, self.sell_eth_price)

    async def update_trump_adv(self):
        if self.trump_active:
            await self.get_trump_competitor()
            self.sell_trump_price = float(self.trump_competitor['adv']['price']) - 1.01
            await updateAdv(self.user, self.user.trump_advNo, self.sell_trump_price)

    async def run(self):
        await self.get_competitor()
        # task2 = asyncio.create_task(self.update_eth_adv())
        # task3 = asyncio.create_task(self.update_btc_adv())
        await asyncio.gather(self.update_btc_adv(), self.update_eth_adv(), self.update_trump_adv())

        await asyncio.sleep(0.5)


path = os.path.abspath("config.json")

with open(path, 'r') as file:
    config = json.load(file)


user = User(config)
script = Script(user)

while script.running:
    os.system('cls')
    asyncio.run(script.run())
