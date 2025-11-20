from string import printable
s=4**36 + 3*4**20 + 4**15 +2*4**7 + 49
res=''
while s!=0:
    res=printable[s%16]+res
    s//=16
print(res)
