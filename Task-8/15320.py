from itertools import product
alph=sorted('ПАРУС')
k=0
for pos,val in enumerate(product(alph,repeat=5),start=1):
    val=''.join(val)
    if val.count('У')<=1 and 'АА' not in val:
        print(pos,val)
        break