from binance import Client


class User:
    def __init__(self, config):
        self.userNo = config['userNo']
        self.api_Key = config['api_Key']
        self.secret_Key = config['secret_Key']
        self.client = Client(self.api_Key, self.secret_Key)

        self.eth_advNo = config['eth_advNo']
        self.btc_advNo = config['btc_advNo']
        self.trump_advNo = config['trump_advNo']

        self.eth_rate = float(self.client.get_symbol_ticker(symbol='ETHUSDT')['price'])
        self.btc_rate = float(self.client.get_symbol_ticker(symbol='BTCUSDT')['price'])
        self.trump_rate = float(self.client.get_symbol_ticker(symbol='TRUMPUSDT')['price'])

        self.minSingleTransAmount = config['minSingleTransAmount']
        self.maxSingleTransAmount = config['maxSingleTransAmount']
        self.min_clearance_eth = config['min_clearance_eth']
        self.min_clearance_btc = config['min_clearance_btc']
        self.min_clearance_trump = config['min_clearance_trump']
        self.headers = {
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/121.0.0.0'
                          'Safari/537.36'
            }
