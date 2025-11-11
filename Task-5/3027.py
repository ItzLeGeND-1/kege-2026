k=0
for n in range(1,5000):
    R=f'{n:b}'
    if n%2==0:
        s=R.count('1')
        h=f'{s:b}'
        R=R+h
    else:
        R='1'+R+'00'
    R=int(R,2)
    if 500<=R<701:
        k+=1
print(k)