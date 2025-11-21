s=729**8 - 3**18 + 85
res=''
while s!=0:
    res=str(s%9)+res
    s//=9
print(res.count('0'))
