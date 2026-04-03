def convert(num):
    res=''
    while num!=0:
        res=str(num%3)+res
        num//=3
    return res
ans=[]
for N in range(1,100000):
    R=convert(N)
    if N%3!=0:
        R='1'+R+R[-3:]
    else:
        R=R+convert(sum(map(int,R))*8)
    R=int(R,3)
    if 1200<=R<=1250:
        ans.append(R)