from string import printable
from itertools import product
k=0
for val in product(printable[:9],repeat=7):
    val=''.join(val)
    if val[0]!='0' and val[0] not in '1357' and int(val[-1])%3!=0 and val.count('6')>=1:
        k+=1
        print(val)
print(k)