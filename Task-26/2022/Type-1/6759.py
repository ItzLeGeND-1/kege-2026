with open(r'../../files/26_6759.txt') as file:
    N=int(file.readline())
    prices=[int(i)for i in file]

amount=N//3
prices=sorted(prices)

customer_check=sum(prices)-sum(prices[-amount:])
shop_check=sum(prices)-sum(prices[::-1][2::3])

print(customer_check,shop_check)