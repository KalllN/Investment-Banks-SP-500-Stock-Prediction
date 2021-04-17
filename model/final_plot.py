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
