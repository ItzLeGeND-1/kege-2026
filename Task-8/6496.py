from itertools import *
k=0
for pos,val in enumerate(product('БЕРСК',repeat=5),start=1):
    val=''.join(val)
    k+=1
for pos,val in enumerate(product('БЕРСК',repeat=6),start=1):
    val=''.join(val)
    k+=1
for pos,val in enumerate(product('БЕРСК',repeat=7),start=1):
    val=''.join(val)
    k+=1
print(k)