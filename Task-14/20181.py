for n in range(1,1000):
    R=f'{n:b}'
    if n%2==0:
        o=f'{sum(map(int,R)):b}'
        R=R+str(o)
    else:
        R='1'+R+'101'
    R=int(R,2)
    if R>350:
        print(n)


