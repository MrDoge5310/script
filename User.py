from binance import Client

config = {
    'api_Key': "AoqvN7WPJiM5LEEgWPHkuxrxUTaYHFPaMI4kfsHujjnuNVhMgJj0oleh75LCN0Tt",
    'secret_Key': "0EQjIMAgmMwc17NaWGbCuUiTtnYDhMWhc7ifwulWmLgcquzU2twQTRdQ6I3zWebh",
    'userNo': 's010efcdd9ed73afca5735774d437ecbd',
    'minSingleTransAmount': 5000,
    'maxSingleTransAmount': 30000,
    'min_clearance': 0.8
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
