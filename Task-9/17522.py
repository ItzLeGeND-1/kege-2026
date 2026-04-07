with open(r'.\file\17522.txt') as file:
    data=[list(map(int,i.split()))for i in file]
cnt=0
for line in data:
    pov=[i for i in line if line.count(i)==2]
    if max(line)<sum(line)-max(line):
        if len(pov)==2:
            cnt+=1
print(cnt)
