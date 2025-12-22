from itertools import product
from string import printable
k=0
for val in product(printable[:20],repeat=5):
    val=''.join(val)
    if val[0]!='0' and int(val[0],20)+int(val[-1],20)==26:
        for i in printable[:20:2]:
            val = val.replace(i, '*')
        for i in printable[1:20:2]:
            val = val.replace(i, '!')
        if val=='!*!*!' or val=='*!*!*':
            k+=1
print(k)
