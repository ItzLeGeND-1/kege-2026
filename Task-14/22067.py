from string import printable
num=3*17**777+15*17**250-6*17**100+2
def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
num17=convert(num,17)
for i in printable[:17:2]:
    num17=num17.replace(i,'*')
print(num17.count('*'))