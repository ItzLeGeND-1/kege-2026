with open(r'.\files\26_6759.txt') as file:
    N=int(file.readline())
    prices=[int(i)for i in file]
sale_amount=N//3
prices=sorted(prices)
customer=sum(prices)-sum(prices[-sale_amount:])
store=sum(prices)-sum(prices[::-1][2::3])
print(customer,store)
