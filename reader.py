import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.pipeline import make_pipeline
from scipy import signal
# import pickle
import pandas as pd
import robin_stocks as r

login = r.login("apetrolino1990@gmail.com", "Poopdick1!")

my_stocks = r.build_holdings()

for key, value in my_stocks.items():
    print(key, value)

plt.rcParams["figure.figsize"] = (22, 9)
basket = ['TCHEY', 'CHK', 'AMD']

## Yahoo finance
import yfinance as yf

# Ticker object of Microsoft stock
msft = yf.Ticker("MSFT")

# Pandas dataframe object
#   shows important features from 1983 - 2019 current day
hist = msft.history(period='max')
# Shows 'High' col for all days from '83-'19
hist["High"]

