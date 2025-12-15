from itertools import product
from string import printable
k=0

for val in product(printable[:12],repeat=7):
    val=''.join(val)
    if val.count('B')==2 and val[0]!='0':
        val = ''.join('*' if int(i) % 2 == 0 else '!' for i in val)
        if '*!*!*!*' in val or '!*!*!*!' in val:
            k+=1
print(k)
