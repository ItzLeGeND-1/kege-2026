with open(r'26_12256.txt') as file:
    S,N=map(int,file.readline().split())
    trucks=[int(i)for i in file]

trucks=sorted(trucks)

ans=[]

for truck in trucks:
    if sum(ans)+truck<=S:
        ans.append(truck)
    if sum(ans[:-1])+truck<=S:
        ans.pop()
        ans.append(truck)
print(len(ans),max(ans))
