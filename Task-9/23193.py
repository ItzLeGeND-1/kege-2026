with open(r'.\file\23193.txt') as file:
    data=[list(map(int,i.split()))for i in file]
for pos,line in enumerate(data,start=1):
    pov=[i for i in line if line.count(i)!=1]
    ne_pov = [i for i in line if line.count(i) == 1]
    if len(pov) == 3 and len(ne_pov) == 3:
        if pov[0]> sum(ne_pov)/3:
            print(pos)