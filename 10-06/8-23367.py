from itertools import product

k=0
for val in product('0123456',repeat=5):
    val=''.join(val)
    if val.count('6')==1 and val.count('00')+val.count('11')+val.count('22')+val.count('33')+val.count('44')+val.count('55')==0 and val[0]!='0':
        print(val)
        k+=1
print(k)