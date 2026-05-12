with open(r'../files/24_23206.txt') as file:
    data=file.readline()

for i in '02468':
    data=data.replace(i,' 0')
data=data.split()
ans=0
for line in data:
    if line.count('S')==35:
        ans=max(ans,len(line))
    if line.count('S')>35:
        while line.count('S')>35:
            line=line[:-1]
        ans = max(ans, len(line))
print(ans)