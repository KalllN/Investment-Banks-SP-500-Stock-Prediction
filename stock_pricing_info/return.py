import numpy as np
import pandas as pd
from pandas import concat
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

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
