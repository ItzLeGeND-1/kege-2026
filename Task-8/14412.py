from itertools import *
k=0
for pos,val in enumerate(product('АЛГОРИТМ',repeat=6),start=1):
    val=''.join(val)
    if val.count('Л')<=1 and val[0]!='Р' and val[-1] not in 'ЛГРТМ':
        k+=1
        print(val)
print(k)