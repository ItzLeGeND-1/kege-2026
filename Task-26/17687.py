with open(r'.\files\26_17687.txt') as file:
    N=int(file.readline())
    prices=[int(i)for i in file]
prices=sorted(prices,reverse=True)

price_count=N//9
luck_price_customer=sum(prices)-sum(prices[:price_count])
real_price_customer=sum(prices)-sum(prices[8::9])
print(luck_price_customer,real_price_customer)