from string import printable
def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return(res)
s=3*3125**8 + 2*625**7 - 4*625**6 +3*125**5 - 2*25**4 - 2025
s25=convert(s,25)
print(s25.count('0'))
