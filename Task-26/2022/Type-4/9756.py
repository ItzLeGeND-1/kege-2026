from pydoc import apropos

with open(r'../../files/26_9756.txt') as file:
    N=int(file.readline())
    events=[list(map(int,i.split()))for i in file]

events=sorted(events,key=lambda x:(x[1],x[0]))

approved=[]
last_minute=0

for event in events:
    if event[0]>=last_minute:
        approved.append(event)
        last_minute=event[1]

approved=approved[:-1]
for event in events[::-1]:
    if approved[-1][1]<=event[0]:
        approved.append(event)

print(len(approved),approved[-1][1])


