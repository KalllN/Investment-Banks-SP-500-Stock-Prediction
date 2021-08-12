import numpy as np
import pandas as pd
from pandas import concat
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

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
