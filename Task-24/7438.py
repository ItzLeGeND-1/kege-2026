with open(r'.\files\24-293.txt') as file:
    data=file.readline()
for i in '02468':
    data=data.replace(i,'*')
data=data.split('D')
ans=0
for i in range(len(data)-100):
    line='D'.join(data[i:i+101])
    if line.count('*')==0 and line.count('DS')+line.count('SD')==0:
        ans=max(ans,len(line))
print(ans)