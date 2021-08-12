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

#Close Price History

plt.figure(figsize = (20, 13))
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
