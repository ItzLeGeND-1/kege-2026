from itertools import product
from string import printable
k=0
for val in product('01234567',repeat=6):
    val=''.join(val)
    if val[0]!='0' and val.count('3')==0 and len(val)==len(set(val)):
        for i in printable[:8:2]:
            val=val.replace(i,'*')
        if "**" in val:
            k+=1
print(k)
