from string import printable
with open(r'../files/24_21908.txt') as file:
    data=file.readline()
for i in printable[14:]:
    data=data.replace(i,' ')
data=data.split()
ans=0
for line in data:
    line=line.lstrip('0').rstrip('13579BD')
    if line:
       ans=max(ans,len(line))
print(ans)
