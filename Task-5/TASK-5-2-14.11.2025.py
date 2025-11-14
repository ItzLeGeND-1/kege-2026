def sector(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return(res)
for n in range(1,1000):
    R=sector(n,4)
    if n%4==0:
        R='2'+R+'03'
    else:
        o=sector((n%4*5),4)
        R=R+o
    R=int(R,4)
    if R<=567:
        print(n)