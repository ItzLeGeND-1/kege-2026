def is_prime(num):
    if num<2: return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True
def fact(num):
    d=[]
    while num%2==0:
        d+=[2]
        num//=2
    i=3
    while i*i<num:
        while num%i==0:
            d+=[i]
            num//=i
        i+=2
    if num>2:
        d+=[num]
    return d
cnt=0
for N in range(3_600_001,10**30):
    d=fact(N)
    if len(d)==3:
        cnt1=0
        for p in d:
            if  str(p) in '35' and is_prime(p):
                cnt1+=1
        if cnt1==3:
         print(N,max(d))
         cnt+=1
         if cnt==5:
            break

