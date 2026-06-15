ans=[]
for N in range(1,1000):
    R=f'{N:o}'
    if R[0]=='5':
        R=R.replace('2','*')
        R = R.replace('1', '2')
        R = R.replace('*', '1')
        R=R+'11'
    else:
        R='2'+R[1:]+'10'
    R=int(R,8)
    if R<1354:
        ans.append([N,R])
print(max(ans))
