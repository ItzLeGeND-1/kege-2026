from string import printable
s=283**382 + 9**15 + 2**3
res=''
while s!=0:
    res=printable[s%14]+res
    s//=14
print(abs(res.count('b')-res.count('c')))
