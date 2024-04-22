from binance import Client


class User:
    def __init__(self, config):
        self.userNo = config['userNo']
        self.api_Key = config['api_Key']
        self.secret_Key = config['secret_Key']
        self.client = Client(self.api_Key, self.secret_Key)

        self.eth_advNo = config['eth_advNo']
        self.btc_advNo = config['btc_advNo']

        self.minSingleTransAmount = config['minSingleTransAmount']
        self.maxSingleTransAmount = config['maxSingleTransAmount']
        self.min_clearance_eth = config['min_clearance_eth']
        self.min_clearance_btc = config['min_clearance_btc']
        self.headers = {
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/121.0.0.0'
                          'Safari/537.36'
            }
