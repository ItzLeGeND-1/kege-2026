o=[]
for n in range(4,1000):
    R=f'{n:b}'
    if n%2==0:
        R=R+R[:3]
    else:
        R='1'+R+'01'
    R=int(R,2)
    if R>600:
       o.append(R)
print(min(o))
