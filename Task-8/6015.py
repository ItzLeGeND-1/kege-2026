from itertools import product
k=0
for val in product('012345678',repeat=7):
    val=''.join(val)
    if val[0]!='0' and val.count('8')==1:
        for i in '02468':
            val=val.replace(i,'*')
        for i in '1357':
            val=val.replace(i,'!')
        if val[-1] not in '*' and val[0] not in '!':
            print(val)
            k+=1
print(k)