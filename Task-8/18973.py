from string import printable
from itertools import product
cnt=0
print(printable[15:25])
for val in product(printable[:25],repeat=4):
    val=''.join(val)
    cnt_15=0
    cnt_che=0
    if val[0]!='0':
        for i in val:
            if i in 'ghijklmno':
                cnt_15+=1
        for i in val:
            if i in printable[:25:2]:
                cnt_che+=1
        if cnt_che>=1 and cnt_15>2:
            cnt+=1
print(cnt)


