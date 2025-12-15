from itertools import product
from string import printable
k=0
for val in product(printable[:16],repeat=3):
    val=''.join(val)
    if val[0]!='0' and len(set(val))==3:
        for i in printable[:16:2]:
            val=val.replace(i,'*')
        for i in printable[1:16:2]:
            val=val.replace(i,'+')
        if val[0]!=val[1] and val[1]!=val[2]:
            k+=1
print(k)


