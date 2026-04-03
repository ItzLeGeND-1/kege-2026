with open(r'.\files\26_4684.txt') as file:
    N=int(file.readline())
    prices=[int(i)for i in file]
sale_count=N//6
prices=sorted(prices)
one_check=sum(prices)-sum(prices[:sale_count])//2
many_check=sum(prices)-sum(prices[::-1][5::6])//2
print(many_check,one_check)