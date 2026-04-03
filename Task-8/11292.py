from string import printable
from itertools import product
k=0
for val in product(printable[:16],repeat=5):
    val=''.join(val)
    if val[0]!='0' and val.count('6')==2:
        for i in printable[:5:2]:
            val=val.replace(i,"*")
        for i in printable[8:16:2]:
            val=val.replace(i,"*")
        if '*6' not in val and '6*' not in val and '66' not in val :
            print(val)
            k+=1
print(k)