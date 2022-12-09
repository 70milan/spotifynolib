import requests
import pandas as pd
from prettytable import PrettyTable
import json


#create a pretty table object
tableobj = PrettyTable()

sec_key = 'cf9a7a2d-736e-400a-8e4a-583205c63667'

#where we extract the data 
api_end = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api_end += sec_key


json_data = requests.get(api_end).json()

cryptodata = json_data['data']


for c in cryptodata:
  c_name = c['name']
  c_symbol = c['symbol']
  c_price = c['quote']['USD']['price']
  c_percent_change_24h = c['quote']['USD']['percent_change_24h']
  c_percent_change_7d = c['quote']['USD']['percent_change_7d']
  c_percent_change_30d = c['quote']['USD']['percent_change_30d']
  tableobj.add_row([c_name, c_symbol, c_price, c_percent_change_24h, c_percent_change_7d, c_percent_change_30d])


tableobj.field_names = ["currency_name","currency_symbol", "price", "percent_change_24h", "percent_change_7d", "percent_change_30d"  ]

table_text = tableobj.get_string()
with open('output.txt', 'w') as file:
  file.write(table_text)

















