from itertools import product
from string import printable
k=0
for val in product(printable[:8],repeat=5):
    val=''.join(val)
    if val[0]=='0' and val[-1] not in '26'and val.count('7')<=2 and int(val[0])%2==0:
        k+=1
print(k)

