from string import printable
def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
for x in range(1,3001):
    s=9*11**210 + 8*11**150 - x
    R=convert(s,11)
    if R.count('0')==60:
        print(x)
