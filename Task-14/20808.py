def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
o=[]
for x in range(1,2031):
    s=7**170+7**100 - x
    s7=convert(s,7)
    if s7.count('0')==73:
        print(x)
