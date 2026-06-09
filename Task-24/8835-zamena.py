with open(r'./files/24-371.txt') as file:
    data=file.readline()
data=data.replace('.','.*')
data=data.split("*")[:-1]
ans=0
for line in data:
    count_M=line.count('M')
    while count_M>112:
        if line[0]=='M': count_M -=1
        line=line[1:]
    if count_M==112:
        ans=max(ans,len(line))
print(ans)