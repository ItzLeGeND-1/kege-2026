ans=[]
def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for n in range(1,1000):
    R=convert(n,3)
    if n%3==0:
        R=R+R[-2:]
    else:
        q=convert(sum(map(int,R))*3,3)
        R=R+q
    R=int(R,3)
    if R>208 and R%2==1:
        ans+=[R]
print(min(ans))
