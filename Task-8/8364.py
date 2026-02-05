from itertools import product

alph=sorted('КРАТЕ')
for pos,val in enumerate(product(alph,repeat=6),start=1):
    val=''.join(val)
    if val=='КАРЕТА':
        print(pos)
    if val=='РАКЕТА':
        print(pos)