from string import printable
with open(r'../files/24_21421.txt') as file:
    data=file.readline().lower()
for i in printable[12:]:
        data=data.replace(i,' ')
data=data.split()
ans=0
for line in data:
    line=line.lstrip('0').rstrip('13579b')
    ans=max(len(line),ans)
print(ans)