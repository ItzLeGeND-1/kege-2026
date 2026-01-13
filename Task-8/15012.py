from string import printable
from itertools import product
k=0
for val in product(printable[:14],repeat=5):
    val=''.join(val)
    if val[0]!='0' and val[-1] in '03':
        q=set(str(val))
        if len(q)==2:
            k+=1
print(k)

