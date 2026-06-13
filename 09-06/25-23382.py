def is_prime(num):
    if num<2: return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True
def fact(num):
    d=[]
    while num%2:
        d+=[2]
        num//=2
    i=3
    while i*i<=num:
        while num%i==0:
            d+=[i]
            num//=i
        i+=2
    if num>2:
        d+=[num]
    return d

cnt=0
for N in range(6_651_220,10**10):
    d=fact(N)
    if len(d)==2 and (str(d)[0]).count('2')+(str(d)[1]).count('2')==2 and is_prime(d[0])and is_prime(d[1]):
        print(N,max(d))
        cnt+=1
        if cnt==5:
            break