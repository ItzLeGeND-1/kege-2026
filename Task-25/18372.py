def f(num):
    d=set()
    for i in range(1,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
        A=sum(d)//len(d)
        if str(A)[-2:]=='12':
            return A
    return 0
cnt=0
for N in range(769_999,0,-1):
    if F:=f(N):
        print(N,F)
        cnt+=1
        if cnt==5:
            break

