ans=[]
def convert(num):
    res=''
    while num:
        res=str(num%3)+res
        num//=3
    return res
for N in range(1,1000):
    R=convert(N)
    if N%3==0:
        R=R+R[-2:]
    else:
        R=R+convert(N%3*5)
    R=int(R,3)
    if R>150:
        ans.append(R)
print(min(ans))
