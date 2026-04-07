with open(r'.\file\17550.txt') as file:
    data=[list(map(int,i.split()))for i in file]
cnt=0
for line in data:
    pov=[i for i in line if line.count(i)!=1]
    ne_pov = [i for i in line if line.count(i) == 1]
    if len(pov)==3 and len(ne_pov)==3:
        if sum(pov)**2> sum(ne_pov)**2:
            cnt+=1
print(cnt)
