def f(num):
    d=set()
    for i in range(1,num+1):
        if num%i==0:
            d|={i,num//i}
    for i in sorted(d):
        S=sum(d)
        if str(S)[-2:]=='23':
            return S
    return 0
for n in range(1_000,10_000):
    if F:=f(n):
        print(n,F)

