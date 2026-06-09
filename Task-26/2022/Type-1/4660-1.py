with open(r'../../files/26_4660.txt') as file:
    N=int(file.readline())
    prods=[int(i)for i in file]
sale_amount=N//4
prods=sorted(prods)
customer_check=sum(prods)-sum(prods[::-1][3::4])//2
shop_check=sum(prods)-sum(prods[:sale_amount])//2
print(customer_check,shop_check)