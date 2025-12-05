
def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
s=15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809
s7=convert(s,7)
che=s7.count('2')+s7.count('6')+s7.count('4')+s7.count('0')
neche=s7.count('1')+s7.count('3')+s7.count('5')
print(abs(che-neche))