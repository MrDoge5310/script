import requests
import json
import hashlib
import hmac
from urllib.parse import urlencode
from check_market import user, client
import time

api_key = user.api_Key
api_secret = user.secret_Key

base_url = "https://api.binance.com"
endpoint = "/sapi/v1/c2c/ads/update"

def generateSignaturedUrl(params, api_secret_ex):
    timestamp = int(time.time() * 1000)
    query_string = urlencode(params)
    # replace single quote to double quote
    query_string = query_string.replace("%27", "%22")
    if query_string:
        query_string = "{}&recvWindow=60000&timestamp={}".format(query_string, timestamp)
    else:
        query_string = "&recvWindow=60000&timestamp={}".format(timestamp)

    signature = hmac.new(api_secret_ex.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
    url = (base_url + endpoint + "?" + query_string + "&signature=" + signature)

    return signature, url

def updateAdv(advNo, price):
    param = {"advNo": advNo, "price": price}

    headers = {"Content-Type": "application/json;charset=utf-8",
               "X-MBX-APIKEY": api_key,
               "clientType": "web"}

    signature, url = generateSignaturedUrl(param, api_secret)
    response = requests.post(url, headers=headers, data=json.dumps(param))
    data = response.json()
    print(data)


