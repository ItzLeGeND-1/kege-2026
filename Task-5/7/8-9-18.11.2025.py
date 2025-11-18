for n in range(1,10000):
    R=f'{n:b}'
    if n%8==0:
        R=R+R[-2:]
    else:
        o=f'{(n%8)*2:b}'
        R=R+o
    R=int(R,2)
    if R>3000:
        print(n)
        break



