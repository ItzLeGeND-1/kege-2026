def sector(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return(res)
for n in range(1,1000):
    R=sector(n,7)
    if sum(map(int,R))%2==0:
        R=R+'555'
    else:
        R='33'+R+'6'
    R=int(R,7)
    if R<12717:
        print(n)
