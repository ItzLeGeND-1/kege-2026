with open(r'.\files\24_10105.txt') as data:
    data=data.readline()
data=data.split('T')
ans=0
for i in range(len(data)-100):
    line='T'.join(data[i:i+101])
    ans=min(ans,len(line))
print(ans)