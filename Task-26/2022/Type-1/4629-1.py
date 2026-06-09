with open(r'../../files/26_4629.txt') as file:
    N=int(file.readline())
    costs=[int(i)for i in file]
ammount=N//4

costs=sorted(costs)
customer_costs=sum(costs)-sum(costs[-ammount:])//2
shop_costs=sum(costs)-sum(costs[:ammount])//2
print(customer_costs,shop_costs)