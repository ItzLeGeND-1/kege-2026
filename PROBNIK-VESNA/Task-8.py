from itertools import product

cnt=0
for val in product('0123456',repeat=7):
    val=''.join(val)
    if val[0] not in '035' and ((val.count('22')>=0 and val.count('44')==0) or (val.count('22')==0 and val.count('44')>=0)):
       cnt+=1
       print(val)
print(cnt)