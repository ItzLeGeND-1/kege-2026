from itertools import *
k=0
for pos,val in enumerate(product('1О1Ь',repeat=5),start=1):
    val=''.join(val)
    if 'ОЬ' not in val and 'ЬЬ' not in val and val[0]!='Ь':
        k+=1
print(k)
