from itertools import product
k=0
for val in product('ABCDEF',repeat=6):
    val=''.join(val)
    if val[0] not in 'AE' and val[-1] not in 'AE':
        print(val)
        k+=1
print(k)