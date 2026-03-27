from itertools import product
cnt=0
for val in product('01234678',repeat=4):
    val=''.join(val)
    if val[0]!='0' and val.count('8')==1:
        num=val.split('8')
        if sum(map(int,num[0]))==sum(map(int,num[1])):
            cnt+=1
print(cnt)
