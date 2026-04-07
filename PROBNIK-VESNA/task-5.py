def convert(num):
    res=''
    while num!=0:
        res=str(num%4)+res
        num//=4
    return res
ans=[]
for N in range(1,1000):
    R=convert(N)
    if N%4==0:
        R=R+R[:2]
    else:
        R=R+convert((N%4)*4)
    R=int(R,4)
    if R>291:
        ans.append(R)
print(min(ans))

