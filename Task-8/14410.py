from itertools import *
k=0
for pos, val in enumerate(product('елносц',repeat=6),start=1):
    val=''.join(val)
    if pos%2==0 and val[0] not in 'ое' and val.count('ц')==2:
        k+=1
print(k)


