from itertools import product
from string import printable
k=0
for val in product(printable[:16],repeat=3):
    val=''.join(val)
    if val[0]!='0':
        numval=val
        if numval[0]>numval[1]>numval[2]:
            k+=1

for val in product(printable[:16],repeat=5):
    val=''.join(val)
    if val[0]!='0':
        numval=val
        if numval[0]>numval[1]>numval[2]>numval[3]>numval[4]:
            k+=1
print(k)