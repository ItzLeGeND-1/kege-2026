from string import printable
def sector(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
k=13
print('41',sector(41,k),'131',sector(131,k))