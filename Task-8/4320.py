from string import printable
from itertools import product
k=0
for val in product(printable[:8],repeat=6):
    val=''.join(val)
    if val[0]!='0' and int(val,8)%5==0 and len(val)==len(set(val)):
        for i in printable[:16:2]:
            val=val.replace(i,'*')
        for i in printable[1:16:2]:
            val=val.replace(i,'!')
        if '**' not in val and '!!' not in val:
           print(val)
           k+=1
print(k)
