def convert(num):
    res=''
    while num!=0:
        res=str(num%5)+res
        num//=5
    return res
for x in range(1,100):
    for y in range(1,100):
        s=5**50 + 5**30 - 5**x - y - 5**y - x
        s5=convert(s)
        if s5.count('0')==10:
            print(x*y)