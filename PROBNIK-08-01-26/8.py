from string import printable
from itertools import product
k=0
for val in product(printable[:25],repeat=4):
    val=''.join(val)
    if val[0]!=0 and val.count('0')+val.count('1')+val.count('2')+val.count('3')+val.count('4')+val.count('5')<=2:
        for i in printable[1:25:2]:
            val=val.replace(i,'*')
        if val.count('*')==1:
            k+=1
            print(val)
print(k)
