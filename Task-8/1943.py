from itertools import *
k=0
for pos,val in enumerate(product('ЗЕРКАЛО',repeat=6),start=1):
    val=''.join(val)
    if val.count('К')<=4 and val.count('З')<=1 and val.count('Е')<=1 and val.count('Р')<=1 and val.count('А')<=1 and val.count('Л')<=1 and val.count('О')<=1 and val.count('К')>0:
        k+=1
print(k)
#for i in 'ЗЕРАЛО':
#    if val.count(i)>1:
#         break
#    else:
#         k+=1