def convert(num):
    res=''
    while num!=0:
        res=str(num%3)+res
        num//=3
    return res
ans=[]
for N in range(1,1000):
    R=convert(N)
    if N%3==0:
        R='1'+R+'02'
    else:
        R=R+convert(N%3*4)
    R=int(R,3)
    if R<100:
        ans+=[N]
print(max(ans))


