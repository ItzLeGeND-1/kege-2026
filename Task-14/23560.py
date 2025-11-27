def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for x in range(1,2401):
    R=convert(7*9**210 + 6*9**110 - x,9)
    if R.count('0')==100:
        print(x)