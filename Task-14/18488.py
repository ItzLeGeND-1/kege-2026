for x in range(1,1000):
    s=7**666 + 7**333 + 49**x - 343
    res=''
    while s:
        res=str(s%7)+res
        s//=7
    if res.count('6')==49:
        print(x)