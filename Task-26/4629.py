with open(r'.\files\26_4629.txt') as file:
    N=int(file.readline())
    price=[int(i)for i in file]
prices=sorted(price)
sale_prods= N//4

customer=sum(prices)-sum(prices[-sale_prods:])//2
store=sum(prices)-sum(prices[:sale_prods])//2
print(customer,store)
