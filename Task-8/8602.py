from itertools import product

slovo=sorted('АЕКНС')

for pos,val in enumerate(product(slovo,repeat=6),start=1):
    val=''.join(val)
    if val=='СЕНЕКА':
        print(pos)