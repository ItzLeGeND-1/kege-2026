s=16**820-2**761+14
res=''
while s>0:
    res=str(s%4)+res
    s//=4
print(res.count('0'))