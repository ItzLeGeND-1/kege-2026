from itertools import product
from string import printable
k=0
for val in product('0123456',repeat=6):
    val=''.join(val)
    if val[0]!='0' and val[-1] not in '0123':
        for i in printable[:7:2]:
            val=val.replace(i,'*')
        if val.count('*')==3:
            k+=1
print(k)
