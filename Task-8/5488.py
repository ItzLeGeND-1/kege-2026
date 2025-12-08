from itertools import *
k=0
for pos,val in enumerate(product('121212',repeat=8),start=1):
    val=''.join(val)
    if val.count('1')>val.count('2'):
        k+=1
print(k)
