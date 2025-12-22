from itertools import product

alph=sorted('ПРЕСТОЛ')
k=0
for pos,val in enumerate(product(alph,repeat=5),start=1):
    val=''.join(val)
    if pos%2==1 and val[-1] in 'ЕО':
        val=val.replace('П','*')
        val = val.replace('Р', '*')
        val = val.replace('С', '*')
        val = val.replace('Т', '*')
        val = val.replace('Л', '*')
        if val.count('*')<=3:
            k+=1
print(k)
