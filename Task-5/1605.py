for N in range(1,1000):
    q=N
    N=N+2
    R=f'{N:b}'
    R=R+str((sum(map(int,R)))%2)
    R = R + str((sum(map(int, R))) % 2)
    R=int(R,2)
    if R<61:
        print(q,R)
