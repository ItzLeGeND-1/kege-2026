def tri(num,sys):
    res=''
    while num!=0:
        res += str(num % sys)
        num//=sys
    return res[::-1]
o=[]
for n in range (1,10000):
    R=tri(n,3)
    if n%3==0:
        R=R+R[-2:]
    else:
        q=n%3*5
        j=tri(q,3)
        R=R+j
    R=int(R,3)
    if R>133:
        o.append(R)
print(min(o))

