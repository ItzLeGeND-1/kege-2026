from itertools import product
from string import printable
k=0
for val in product(printable[:7],repeat=7):
    val=''.join(val)
    if val[0]!='0':
        for i in printable[:7:2]:
            val = val.replace(i, '*')
        if val.count('*')==2:
            k+=1
print(k)