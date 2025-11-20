s=51*7**12-7**3-22
res=''
while s>0:
    res=str(s%7)+res
    s//=7
print(sum(map(int,res)))