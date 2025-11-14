for n in range(2,10000):
    R=f'{n:b}'
    cnt_1=R[1::2].count('1')
    cnt_0=R[::2].count('0')
    R=abs(cnt_1-cnt_0)
    if R==5:
        print(n)
        break