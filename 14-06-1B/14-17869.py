from string import printable
def convert(num):
    res=''
    while num:
        res=printable[num%25]+res
        num//=25
    return res
s=3*3125**8 + 2*625**7 - 4*625**6 +3*125**5 -2*25**4 - 2025
s25=convert(s)
print(s25.count('0'))