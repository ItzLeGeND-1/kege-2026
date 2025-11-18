u=[]
o=[]
def sector(num,sys):
    res=''
    while num !=0:
        res=str(num%sys)+res
        num//=sys
    return res
for n in range(1,10000):
    R=sector(n,3)
    if n%2==0:
        R=R+R[-2:]
    else:
        q=sector(sum(map(int,R)),3)
        R=R+q
    R=int(R,3)
    if R==82:
        print(n)




