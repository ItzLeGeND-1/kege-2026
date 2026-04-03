from itertools import product
k=0
for val in product('0123456',repeat=5):
    val=''.join(val)
    if val[0]!='0':
        for i in '0246':
            val=val.replace(i,'*')
        for x in '1357':
            val=val.replace(x,'!')
        if val.count('**')>=2 and val.count('***')==0:
            k+=1
            print(val)
print(k)