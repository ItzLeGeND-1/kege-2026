s=5*343**2031 + 4*49**2142 - 3*7**111 +7**222
res=''
while s!=0:
    res=str(s%7)+res
    s//=7
print(sum(map(int,res)))