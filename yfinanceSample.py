# Extracting Stock Data Using a Python Library
''' 
!pip install yfinance==0.2.4
!pip install pandas==1.3.3
$ pip install yfinance --upgrade --no-cache-dir
'''
import yfinance as yf
import pandas as pd
# Using the Ticker module we can create an object that will allow us to access functions to extract data
apple = yf.Ticker("AAPL")
# get stock info
''' apple.info '''
# !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
''' apple_info '''
''' apple_info['country'] '''
pple_share_price_data = apple.history(period="max")
'''apple_share_price_data.head()'''
apple_share_price_data.reset_index(inplace=True)
'''apple_share_price_data.plot(x="Date", y="Open")'''
# Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns
'''apple.dividends.plot()'''
