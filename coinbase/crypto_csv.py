import requests
import pandas as pd
from prettytable import PrettyTable
import os
import csv
import json


#create a pretty table object
tableobj = []
csvheaders = ["currency_name","currency_symbol", "price", "percent_change_24h", "percent_change_7d", "percent_change_30d"]



sec_key = 'cf9a7a2d-736e-400a-8e4a-583205c63667'

#where we extract the data 
api_end = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api_end += sec_key


json_data = requests.get(api_end).json()

cryptodata = json_data['data']


for c in cryptodata:
  listings = [c['name'], c['symbol'], c['quote']['USD']['price'],
  c['quote']['USD']['percent_change_24h'], c['quote']['USD']['percent_change_7d'],
  c['quote']['USD']['percent_change_30d']] 
  tableobj.append(listings)



with open('crypto.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csvheaders)
    writer.writerows(tableobj)
