for n in range(1,1000):
    R=f'{n:b}'
    if n%5==0:
        R=R+R[-3:]
    else:
        s=(n%5)*5
        q=f'{s:b}'
        R=R+q
    R=int(R,2)
    if R>256:
        print(n)
        break
