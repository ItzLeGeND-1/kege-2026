from string import printable
def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
s=2*2401**525+3*343**524-4*49**523+5*49**522-6*7**521-35
d49=convert(s,49)
k=0
for i in range(1,10):
    k+=d49.count(str(i))
print(k)
