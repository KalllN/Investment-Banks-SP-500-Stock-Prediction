import numpy as np
import pandas as pd
from pandas import concat
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

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
