with open(r'./files/26_21598.txt') as file:
    N=int(file.readline())
    times=[list(map(int,i.split()))for i in file]

timeline=[0]*1440

for time in times:
    for i in range(time[0],time[1]):
        timeline[i]+=1
cnt_max=0
cnt=1
for t1,t2 in zip(timeline,timeline[1:]):
    if t1==t2!=0:
        cnt+=1
    else:
        cnt_max=max(cnt,cnt_max)
        cnt=1
    cnt_max = max(cnt, cnt_max)
print(cnt_max,timeline)