def tri(num,sys):
    res=''
    while num !=0:
        res=str(num%sys)+res
        num//=sys
    return res
for n in range(1,1000):
    R=tri(n,3)
    if n%3==0:
        R='1'+R+'02'
    else:
        u=n%3*4
        i=tri(u,3)
        R=R+i
    R=int(R,3)
    if R<199:
        print(n)
