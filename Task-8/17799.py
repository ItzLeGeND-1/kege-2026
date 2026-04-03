from itertools import product
print(sorted('АРГУМЕНТ'))
alph=sorted('АРГУМЕНТ')
for pos,val in enumerate(product(alph,repeat=4),start=1):
    val=''.join(val)
    if val=='НРТУ':
        print(pos)
