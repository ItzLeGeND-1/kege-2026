ans=[]
def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for N in range(1,10000):
    R=convert(N,7)
    if R[-1]=='2':
        R=R.replace('3','*')
        R = R.replace('1', '3')
        R = R.replace('*', '1')
        R='21'+R
    else:
        R='1'+R[1:]+'36'
    R=int(R,7)
    if R==664:
        print(N)