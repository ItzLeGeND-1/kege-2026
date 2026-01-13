from itertools import product

alph=sorted('НОРМАЛЬЕ')

for pos,val in enumerate(product(alph,repeat=6),1):
    val=''.join(val)
    if 'НОРМ' in val[0:4]:
        print(pos)
        break
    if 'НЕНОРМ' in val:
        print(pos)