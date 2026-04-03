from itertools import product
cnt=0
for val in product('0123456',repeat=5):
    val=''.join(val)
    if val[0]!='0' and val.count('3')+val.count('4')+val.count('5')==2 and '00' not in val and '11' not in val and '22' not in val and '33' not in val and '44' not in val and '55' not in val and '66' not in val:
        cnt+=1
        print(val)
print(cnt)
