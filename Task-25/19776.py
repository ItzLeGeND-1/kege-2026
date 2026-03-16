def is_prime(num):
    if num<2: return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True

def f(num):
    d=set()
    for i in range(1,int(num**.5)+1):
        if num%i==0:
            if is_prime(i): d|={i}
            if is_prime(num//i): d |= {num//i}
    if len(d)>1:
        M=min(d)+max(d)
        if M%213==171:
            return M
    return False
cnt=0
for N in range(23_600_000+1,10**10):
    if M:=f(N):
        cnt+=1
        print(N,M)
        if cnt==6:
            break
