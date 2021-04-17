import numpy as np
import pandas as pd
from pandas import concat
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import pandas_datareader as web

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
    
    plt.xlabel("Date: 2013-02-08 to 2018-02-07")
    plt.ylabel("Close price")
    plt.title(f"{bank_name[i - 1]} Stock Movement")
    plt.legend(loc = "upper left")
