with open(r'26_9756.txt') as file:
    N=int(file.readline())
    times=[list(map(int,i.split()))for i in file]
times=sorted(times,key=lambda x:(x[1],x[0]))

conferences=[times[0]]

for event in times:
    if conferences[-1][-1]<=event[0]:
        conferences.append(event)
conferences=conferences[:-1]

for event in times[::-1]:
    if conferences[-1][-1]<=event[0]:
        conferences.append(event)
        break
print(conferences[-1])