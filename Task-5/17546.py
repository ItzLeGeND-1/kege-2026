o=[]
for n in range(1,1000):
    R=f'{n:b}'
    if n%2==0:
        R='10'+R
    else:
        R='1'+R+'01'
    R=int(R,2)
    if n<=12:
        o.append(R)
print(max(o))

