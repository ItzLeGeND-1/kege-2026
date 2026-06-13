with open(r'26_17643.txt')as file:
    N=int(file.readline())
    product=[list(map(int,i.split()))for i in file]
product=sorted(product,key=lambda x:(-x[1],x[0],x[2]))
d=set()
for i in product:
    d|={i[0]}
ans=0
for articul in d:
    cnt=0
    if articul!=product[0]:
        continue
    if articul==product[0]:
        if product[0]==0:
            cnt+=1
    ans=max(ans,cnt)
print(ans)


