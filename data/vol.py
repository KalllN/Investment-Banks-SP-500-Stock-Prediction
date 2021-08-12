#Daily Volume
plt.figure(figsize = (20, 13))
for i, bank in enumerate(ib_bank_list, 1):
    plt.subplot(2, 2, i)
    bank["volume"].plot(color = "red")
    plt.ylabel("Volume")
    plt.xlabel("Days")
    plt.title(f"{bank_name[i - 1]}")
