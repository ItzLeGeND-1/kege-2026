from string import printable
from itertools import product
a=0
for val in product(printable[:15],repeat=5):
    val=''.join(val)
    if val[0]!='0' and val.count('8')==1:
        k=0
        for x in printable[10:15]:
            k+=val.count(x)
        if k>=2:
           a+=1
print(a)
