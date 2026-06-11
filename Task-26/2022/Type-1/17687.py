with open(r'../../files/26_17687.txt') as file:
    N=int(file.readline())
    costs=[int(i)for i in file]
amount=N//9

costs=sorted(costs)

customer_check=sum(costs)-sum(costs[-amount:])
shop_check=sum(costs)-sum(costs[::-1][8::9])
print(customer_check,shop_check)