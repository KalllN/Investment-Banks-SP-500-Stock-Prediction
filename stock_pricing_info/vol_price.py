import numpy as np
import pandas as pd
from pandas import concat
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Correlation between Volume and High Price USD ($)
matplotlib.pyplot.figure(figsize = (20, 13))

for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    sns.scatterplot(x = bank['volume'], y = bank['high'], color = 'purple')
    plt.title(f"{ib_list[i - 1]}")
