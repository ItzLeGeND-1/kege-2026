def sector(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return(res)
for n in range(1,10000):
    R=sector(n,4)
    if R[0]=='3':
        R=R.replace('1','5')
        R=R.replace('3','1')
        R=R.replace('5','3')
        R='21'+R
    else:
        R='1'+R[1:]+'12'
    R=int(R,4)
    if R<598:
        print(n)