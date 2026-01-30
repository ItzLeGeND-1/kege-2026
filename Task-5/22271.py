ans=[]
for N in range(1,1000):
    R=f'{N:o}'
    if R[0]=='5':
        R=R.replace('2','*')
        R = R.replace('1', '2')
        R = R.replace('*', '1')
        R='11'+R
    else:
        R='+2'+R[1:]+'10'
    R=int(R,8)
    if R==1352:
        print(N)
