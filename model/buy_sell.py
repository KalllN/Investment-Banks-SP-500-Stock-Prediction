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
