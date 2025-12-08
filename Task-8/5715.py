from itertools import *
k=0
for pos,val in enumerate(product('123',repeat=15),start=1):
    val=''.join(val)
    if val.count('1')>val.count('2')>val.count('3'):
        k+=1
print(k)