for n in range(10000,100000):
    o=str(n)
    q=[]
    k=1
    a=''
    for i in range(5):
        q.append(o[i])
    j=(int(max(q))+int(min(q)))**2
    for i in range(5):
        if int(o[i])%2==0:
            k=k*int(o[i])
    if j>k:
        a=str(j)+str(k)
    else:
        a=str(j)+str(i)
    if a=='12116':
        print(n)

