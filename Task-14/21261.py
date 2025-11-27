from string import printable
def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
for n in range(1,1000):
    R=convert(n,4)
    if sum(map(int,R))%3==0:
        R=R.replace('0','5')
        R=R.replace('2','0')
        R=R.replace('5','2')
        R='32'+R
    else:
        R=R+'33'
        R=R.replace(R[2:4],'10')
    R=int(R,4)
    if R>320:
        print(n)
        break