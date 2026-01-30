from itertools import product
from string import printable
k=0
for val in product(printable[:16],repeat=4):
    val=''.join(val)
    if val[0]!='0' and val.count('9')==1:
        for i in printable[0:16:2]:
            val=val.replace(i,'*')
        for i in printable[1:16:2]:
            val=val.replace(i,'!')
        if '!!' not in val and '**' not in val:
            print(val)
            k+=1
print(k)
