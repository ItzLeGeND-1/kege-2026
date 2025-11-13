def sector(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return(res)
for n in range(1,1000):
    R=sector(n,8)
    if R.count('2')+R.count('4')+R.count('6')+R.count('0')%2==0:
        R=R+'46'
    else:
        o=(n%8)*5
        q=f'{o:o}'
        R=q+R
    R=int(R,8)
    if n>=80:
        print(R)
        break