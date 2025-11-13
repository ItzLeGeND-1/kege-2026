for n in range(1,1000):
    R=f'{n:b}'
    if R.count('1')%2==0:
        R='10'+R[2:]+'0'
    else:
        R='11'+R[2:]+'1'
    R=int(R,2)
    if n>27:
        print(R)
        break