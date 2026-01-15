from itertools import product
from string import printable
k=0
for val in product('012345678',repeat=7):
    val=''.join(val)
    if val[0]!='0' and val.count('2')==0 and len(val)==len(set(val)):
        for i in printable[0:9:2]:
            val=val.replace(i,'*')
        for i in printable[1:9:2]:
            val=val.replace(i,'!')
        if '!!' not in val and '**' not in val:
          k+=1
print(k)

