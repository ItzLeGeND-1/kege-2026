k=0
for n in range(1,1000):
    R=f'{n:x}'
    if R.count("b")%2==0:
        R='1'+R
    else:
        R=R+'1'
    R=int(R,16)
    if len(str(R))==2:
        k+=1
print(k)

