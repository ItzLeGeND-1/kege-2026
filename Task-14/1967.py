from string import printable
s=3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1
res=''
while s!=0:
    res=printable[s%16]+res
    s//=16
print(res.count('0'))
