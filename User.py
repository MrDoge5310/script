from binance import Client

config = {
    'api_Key': '6HC8gJQtWG4UbEVb5usCD8EhuddBkqJ4XJD04JF4j4e03vbt9WMRP3PBXBcOgLoA',
    'secret_Key': 'q1jfzQ77JvLtCmlMtBG7ynNySoz1sPO42sWTXQ3G9m4gncDiUg4bEll8vyJYpdG0',
    'userNo': 'se6a51d75f40c33c6a595377d66227984',
    'minSingleTransAmount': 5000,
    'maxSingleTransAmount': 75000,
    'min_clearance': 0.4
}


class User:
    def __init__(self):
        self.userNo = config['userNo']
        self.api_Key = config['api_Key']
        self.secret_Key = config['secret_Key']
        self.minSingleTransAmount = config['minSingleTransAmount']
        self.maxSingleTransAmount = config['maxSingleTransAmount']
        self.min_clearance = config['min_clearance']
        self.headers = {
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/121.0.0.0'
                          'Safari/537.36'
            }

    def create_Client(self):
        return Client(self.api_Key, self.secret_Key)
