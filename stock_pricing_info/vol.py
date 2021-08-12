import numpy as np
import pandas as pd
from pandas import concat
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Daily Volume
plt.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    bank["volume"].plot(color = "red")
    plt.ylabel("Volume")
    plt.xlabel("Days")
    plt.title(f"{bank_name[i - 1]}")
