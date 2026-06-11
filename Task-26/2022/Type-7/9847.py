with open(r'../../files/26_9847.txt') as file:
    N=int(file.readline())
    times=[list(map(int,i.split()))for i in file]

minutes=[0]*1440

for time in times:
    for i in range(time[0],time[1]):
        minutes[i]+=1
ans=[]
for i in range(len(minutes)):
    if minutes[i]==643:
        ans.append(i)
cnt=1
for num1,num2 in zip(ans,ans[1:]):
    if num2-num1>1:
        cnt+=1

print(cnt,max(minutes))

