import requests
from bs4 import BeautifulSoup
import time
import json
import urllib.parse
import os
import sys

# set the headers and user string
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
telegram_api_url = 'https://api.telegram.org/bot1285768969:AAFHIg8menF4c5w-Fzo36wjBOI5bjqCMh1s/sendMessage?chat_id=22734488&text='

json_file = os.path.join(sys.path[0], "db.json")


def check_price(_url, _price, lowest_price):

  response = requests.get(_url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  soup.encode('utf-8')
  
  if(soup.find(id="priceblock_ourprice") == None):
    return []
  price = soup.find(id="priceblock_ourprice").get_text().replace(
      ',', '').replace('€', '').replace(' ', '').strip()
  converted_price = int(price)
  if(converted_price < lowest_price):
    obj = json.dumps(
        {'OCCAZIONE': 'TRUE', 'url': _url, 'price': converted_price})
    obj = urllib.parse.quote(obj)
    telegram = telegram_api_url+obj
    requests.get(telegram, headers=headers)
    return [converted_price, True]
  elif(converted_price < _price):
    obj = json.dumps(
        {'OCCAZIONE': 'FALSE', 'url': _url, 'price': converted_price})
    obj = urllib.parse.quote(obj)
    telegram = telegram_api_url+obj
    requests.get(telegram, headers=headers)
    return [converted_price, False]
  return []

def main():
  data = None
  f = open(json_file, 'r')
  data = json.load(f)
  f.close()
  for i, product in enumerate(data, start=0):
    new_price = check_price(
        product['url'], product["price"], product["lowest_price"])
    if(len(new_price) != 0):
      if(new_price[1] == True):
        data[i]["lowest_price"] = new_price[0]
      else:
        data[i]["price"] = new_price[0]
  f = open(json_file, 'w')
  json_object = json.dumps(data)
  f.write(json_object)
  f.close()

if __name__ == "__main__":
    while(true):
      main()
      time.sleep(60*5)

