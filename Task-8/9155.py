from itertools import *
k=0
for pos,val in enumerate(product('ЬРПЛЕА',repeat=5),start=1):
    val=''.join(val)
    if val[-1]=='Ь' and pos<=387:
        k+=1
print(k)
