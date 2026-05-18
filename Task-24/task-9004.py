with open(r'./files/24-384.txt') as file:
    data=file.readline()
data=data.split('Z')
ans=10000000000000000000
for i in range(len(data)-270):
    line='Z'.join(data[i:i+271])
    ans=min(ans,line)
print(ans)