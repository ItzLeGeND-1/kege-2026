from itertools import *
k=0
for pos,val in enumerate(product('ГЕПАРД', repeat=5),start=1):
    val=''.join(val)
    if val.count('Г')==1 and val[0] not in 'А' and val[-1] not in 'Е':
        k+=1
print(k)
