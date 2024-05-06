import requests
import json
import hashlib
import hmac
from urllib.parse import urlencode
import time

base_url = "https://api.binance.com"
endpoint = "/sapi/v1/c2c/ads/update"
server_time = requests.get(base_url + "/api/v3/time").json()
server_time = int(server_time["serverTime"])
client_time = int(time.time()*1000)
recvWindow = server_time - client_time


def generateSignaturedUrl(params, api_secret_ex):
    timestamp = int(time.time() * 1000) + recvWindow
    query_string = urlencode(params)
    # replace single quote to double quote
    query_string = query_string.replace("%27", "%22")
    if query_string:
        query_string = "{}&recvWindow=30000&timestamp={}".format(query_string, timestamp)
    else:
        query_string = "&recvWindow=60000&timestamp={}".format(timestamp)

    signature = hmac.new(api_secret_ex.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
    url = (base_url + endpoint + "?" + query_string + "&signature=" + signature)

    return signature, url


def updateAdv(user, advNo, price):
    param = {"advNo": advNo, "price": price}

    headers = {"Content-Type": "application/json;charset=utf-8",
               "X-MBX-APIKEY": user.api_Key,
               "clientType": "web"}

    signature, url = generateSignaturedUrl(param, user.secret_Key)
    try:
        response = requests.post(url, headers=headers, data=json.dumps(param))
        data = response.json()
        print(data)
    except:
        print("Ошибка отправки запроса")
