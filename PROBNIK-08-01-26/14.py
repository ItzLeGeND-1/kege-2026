ans=[]
def convert(num,sys):
    res=''
    while num!=0:
        res=str(num%sys)+res
        num//=sys
    return res
for x in range(10,70001):
    s=5**2025 + 5**400 - x
    s5=convert(s,5)
    ans.append(s5.count('4'))
print(max(ans))
