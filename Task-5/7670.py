o=[]
for n in range(151,10000):
    R=f'{n:x}'
    R=R.replace('a','1')
    cnt_chet=0
    for i in R:
        if i in '02468ace':
            cnt_chet+=1
    if cnt_chet>2:
        R=R+'b'
    else:
        R='f'+R
    R=int(R,16)
    if R>3500:
        o+=[R,n]
print(o)
if [1 for i in R if i in '02468ace']