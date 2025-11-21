o=[]
def sector(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for n in range(1,10000):
    R=sector(n,3)
    if sum(map(int,R))%3==0:
        R=R+'212'
    else:
        q=sector(sum(map(int,R))*2,3)
        R=R+q
    R=int(R,3)
    if R>490:
        o+=[R]
print(min(o))