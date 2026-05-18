
with open(r'.\files\24_21717.txt') as data:
    data=data.readline()
data=data.split('RSQ')
ans=100000000000000000
k='Z'*10000
for i in range(len(data)-130):
    line='RSQ'.join(data[i:i+131])
    ans=min(ans,len(line))
    k=min(k,line)
print(ans,k)