with open(r'.\files\24_25361.txt') as data:
    data=data.readline()

for i in '02468':
    data=data.replace(i, ' 0')
data=data.split()
ans=0
for i in data:
    if i[0] == '0' and i.count('F')==76:
        ans=max(ans,len(i))
    if i[0] == '0' and i.count('F')>76:
        while i.count('F')>76:
           pos_F=i.rfind('F')
           i=i[:pos_F]
        ans = max(ans, len(i))
print(ans)