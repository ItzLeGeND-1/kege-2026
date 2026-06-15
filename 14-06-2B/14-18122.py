def convert(num):
    res=''
    while num:
        res=str(num%5)+res
        num//=5
    return res
for x in range(1,5556):
    s=5**150 + 5**135 - x
    s5=convert(s)
    if s5.count('4')==134:
        print(x)