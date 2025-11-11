ans=[]
for n in range(1,10000):
    R=f'{n:b}'
    if n%3==0:
        R=R+R[-3:]
    else:
        q=(n%3)*3
        s=f'{q:b}'
        R=R+s
    R=int(R,2)
    if R<170:
        ans.append(R)
print(max(ans))
