def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return resddd
for x in range(1,2301):
    d=7**350 + 7 ** 150 - x
    d7=convert(d,7)
    if d7.count('0')==200:
        print(x)