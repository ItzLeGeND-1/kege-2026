from itertools import product
from string import printable

k=0

for val in product(printable[:2],repeat=16):
    val=''.join(val)
    if val.count('1')%3==0:
        k+=1
        print(val)
print(k)