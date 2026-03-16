ans=[]
for N in range(1,10000):
    R=f'{N:b}'
    if N%3==0:
        R=R+R[-3:]
    else:
        q=f'{N%3*3:b}'
        R=R+q
    R=int(R,2)
    if 100<=R<=140:
        

