ans=[]
def f(num):
    res=''
    while num:
        res=str(num%3)+res
        num//=3
    return res
for N in range(1,1000):
    R=f(N)
    if N%3==0:
        R='1'+R+'02'
    else:
        R=R+f(N%3*4)
    R=int(R,3)
    if R<100:
        ans.append([R,N])
print(max(ans))