o=[]
def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for x in range(1,10000):
    s=7**270 + 7 **170+7**70-x
    s7=convert(s,7)
    if s7.count('0')==203:
        print(x)
