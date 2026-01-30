ans=[]
def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res if res else '0'
for N in range(0,1000):
    R=convert(N,4)
    if N%2==0:
        R='12'+R
        q=int(R[-1])*3
        R=R+convert(q,4)
    else:
        R='13'+R+"21"
    R=int(R,4)
    if R>50:
        print(R)
        ans.append(R)
print(min(ans))