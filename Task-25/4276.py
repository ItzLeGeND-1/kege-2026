def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    if len(d)>=7:
        cnd=sorted(d)[-7]
        return cnd
    return 0
def j(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    if len(d)>=7:
        cnd=sorted(d)[-7]
        return len(d)
    return 0
cnt=0
for N in range(400_000_001,10**20):
    q=j(N)
    if D:=f(N):
        print(D,q)
        cnt+=1
        if cnt==5:
            break

