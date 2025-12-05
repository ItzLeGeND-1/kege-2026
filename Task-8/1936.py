from itertools import *
k=0
for pos,val in enumerate(product('ПСКАЛЬ',repeat=4),start=1):
    val=''.join(val)
    if val[0] not in 'Ь' and 'ЬЬ' not in val:
        k+=1
print(k)