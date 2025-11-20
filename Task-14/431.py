def sector(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for x in range(1,1000):
    ura=3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x)+1*7**(2*x)
    sem=sector(ura,7)
    if sum(map(int,sem))==18:
        print(x)