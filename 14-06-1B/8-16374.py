from itertools import product
k=0
for val in product('01*3*5*',repeat=7):
    val=''.join(val)
    if val[0]!='0' and val.count('0')+val.count('*')==2:
        k+=1
print(k)