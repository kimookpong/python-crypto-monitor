"""
Author: Mr. Hakim Mudor
FileName: test.py
Desc: description
Created:  Fri Mar 19 2021
"""

import hashlib
import hmac
import json
import requests

# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = 'API_KEY'
API_SECRET = b'API_SECRET'


def json_encode(data):
    return json.dumps(data, separators=(',', ':'), sort_keys=True)


def sign(data):
    j = json_encode(data)
    print('Signing payload: ' + j)
    h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
    return h.hexdigest()


# check server time
response = requests.get(API_HOST + '/api/servertime')
ts = int(response.text)
print('Server time: ' + response.text)

# check balances
header = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-BTK-APIKEY': API_KEY,
}
data = {
    'ts': ts,
}
signature = sign(data)
data['sig'] = signature

print('Payload with signature: ' + json_encode(data))
#response = requests.post(API_HOST + '/api/market/balances',headers=header, data=json_encode(data))

#print('Balances: ' + response.text)


def symbol():
    response = requests.get(API_HOST + '/api/market/symbols')
    print(response.text)


def ticker():
    response = requests.get(
        API_HOST + '/api/market/ticker', params='sym=THB_XRP')
    print(response.text)


def bids():
    response = requests.get(API_HOST + '/api/market/bids',
                            params='sym=THB_BTC&lmt=1')
    print(response.text)


ticker()
