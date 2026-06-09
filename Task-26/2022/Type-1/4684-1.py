from idlelib.help import copy_strip

with open(r'../../files/26_4684.txt') as file:
    N=int(file.readline())
    prices=[int(i)for i in file]
ammount=N//6
prices=sorted(prices)
many_check=sum(prices)-sum(prices[::-1][5::6])//2
one_check=sum(prices)-sum(prices[:ammount])//2
print(many_check,one_check)