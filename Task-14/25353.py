from string import printable

def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
for x in range(1,27001):
    s=3*27**9 + 2*27**6 + 27**3 - x
    s27=convert(s,27)
    if s27.count('0')==6:
        print(x)
        break