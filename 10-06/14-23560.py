def f(num):
    res=''
    while num:
        res=str(num%9)+res
        num//=9
    return res
for x in range(0,2401):
    s=7*9**210 + 6*9**110 - x
    s9=f(s)
    if s9.count('0')==100:
        print(x)
