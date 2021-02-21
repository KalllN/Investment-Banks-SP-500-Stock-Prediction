import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import concat
import matplotlib
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import pandas_datareader as web
import datetime as dt

#Loading data
#from google.colab import files #opens files in computer
#uploaded = files.upload()
JPM = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/JPM_data.csv')
BOA = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/BAC_data.csv')
CITI = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/C_data.csv')
GS = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/GS_data.csv')

JPM['date'] = pd.to_datetime(JPM['date'])
BOA['date'] = pd.to_datetime(BOA['date'])
CITI['date'] = pd.to_datetime(CITI['date'])
GS['date'] = pd.to_datetime(GS['date'])

ib_list = ['JPM', 'BOA', 'CITI', 'GS']
ib_bank_list = [JPM, BOA, CITI, GS]
bank_name = ['JP Morgan', 'Bank of America', 'Citi', 'Goldman Sachs']
for i, bank in enumerate(ib_bank_list, 1):
    bank['Name'] = bank_name[i-1]

#EDA
#Relationship between Opening & Closing Price USD($)
plt.figure(figsize = (21, 12))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    plt.hist([bank['open'], bank['close']], color = ["dodgerblue", "lightsalmon"])
    plt.ylabel("Opening & Closing Price USD($)")
    plt.xlabel("No. of days")
    plt.title(f"{bank_name[i - 1]}")

#Correlation of High & Low Stock Prices USD ($)
plt.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    plt.plot(bank['date'], bank[['high','low']])
    plt.xlabel("Year")
    plt.ylabel("High & Low Prices USD($)")
    plt.title(f"{bank_name[i - 1]}")

#Daily Volume
plt.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    bank["volume"].plot(color = "red")
    plt.ylabel("Volume")
    plt.xlabel("Days")
    plt.title(f"{bank_name[i - 1]}")

#Close Price History
plt.figure(figsize = (20, 13))
sma30 = []
sma100 = []
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    avg30day = pd.DataFrame()
    avg30day['close'] = bank['close'].rolling(window = 30).mean()
    sma30.append(avg30day)
    avg100day = pd.DataFrame()
    avg100day['close'] = bank['close'].rolling(window = 100).mean()
    sma100.append(avg100day)
    plt.plot(bank['close'], label = f"{ib_list[i - 1]}")
    plt.plot(avg30day['close'], label = 'SMA30')
    plt.plot(avg100day['close'], label = 'SMA100')
    plt.title(f"{bank_name[i - 1]}")
    plt.xlabel("Date: 2013-02-08 to 2018-02-07")
    plt.ylabel("Close price")
    plt.legend(loc = "upper left")

#Correlation between Volume and High Price USD ($)
matplotlib.pyplot.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    sns.scatterplot(x = bank['volume'], y = bank['high'], color = 'purple')
    plt.title(f"{ib_list[i - 1]}")

#Daily Return
plt.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    bank['Daily Return'] = bank['close'].pct_change()
    sns.distplot(bank['Daily Return'].dropna(),bins = 2000, color = "gold")
    plt.ylabel('Close Price')
    plt.title(f"{bank_name[i - 1]}")

for i, bank in enumerate(ib_bank_list, 1):
    bank['avg30day'] = sma30[i-1]
    bank['avg100day'] = sma100[i-1]
    i += 1

#Buy & Sell Model
def stock_interpretation(comp):
    buy, sell, c = [], [], -1
    for i in range(len(comp)):
        if(comp['avg30day'][i] > comp['avg100day'][i]): #i is the position of the graph
            if c != 1:
                buy.append(comp['close'][i])
                sell.append(np.nan)
                c = 1
            else:
                buy.append(np.nan)
                sell.append(np.nan)
        elif(comp['avg30day'][i] < comp['avg100day'][i]):
            if c!= 0:
                buy.append(np.nan)
                sell.append(comp['close'][i])
                c = 0
            else:
                buy.append(np.nan)
                sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    return(buy, sell)

#Cannot run a loop for the below code since same object name gives a type error
o1 = stock_interpretation(JPM)
JPM['buy'] = o1[0]
JPM['sell'] = o1[1]
o2 = stock_interpretation(BOA)
BOA['buy'] = o2[0]
BOA['sell'] = o2[1]
o3 = stock_interpretation(CITI)
CITI['buy'] = o3[0]
CITI['sell'] = o3[1]
o4 = stock_interpretation(GS)
GS['buy'] = o4[0]
GS['sell'] = o4[1]

#Stock Movement
plt.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)   
    plt.plot(bank['close'], label = f"{ib_list[i - 1]}", alpha = 0.3)
    plt.plot(bank['avg30day'], label = 'SMA30', alpha = 0.3)
    plt.plot(bank['avg100day'], label = 'SMA100', alpha = 0.3)
    plt.scatter(bank.index, bank['buy'], label = 'buy', marker = "^", color = "green", s = 200)
    plt.scatter(bank.index, bank['sell'], label = 'sell', marker = "v", color = "red", s = 200)
    plt.title(f"{bank_name[i - 1]} Stock Movement")
    plt.legend(loc = "upper left")
    plt.xlabel("Date: 2013-02-08 to 2018-02-07")
    plt.ylabel("Close price")
