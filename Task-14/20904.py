def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res

for x in range(1,2031):
    num1=3**100-x
    num3=convert(num1,3)
    if num3.count('0')==1:
        print(x)
