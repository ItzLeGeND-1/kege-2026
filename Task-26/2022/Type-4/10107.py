with open(r'../../files/26_10107.txt') as file:
    N=int(file.readline())
    times=[list(map(int,i.split()))for i in file]

times=sorted(times,key=lambda x:(x[1],x[0]))

conferences=[times[0]]

for event in times:
    if conferences[-1][1]<=event[0]:
        conferences.append(event)
print(conferences)
print(len(conferences))
ans=[]
conferences=conferences[:-1]
conferences.append(max(times))v

print(len(conferences),conferences[-1][0]-conferences[-2][1])