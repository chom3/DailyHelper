import requests
from SendText import *

headers = {
    'Content-Type': 'application/json'
}

requestResponse = requests.get(f"https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token={token}", headers=headers)
print(requestResponse.json())


a = """\

This message is sent from Python."""

sendText(a)