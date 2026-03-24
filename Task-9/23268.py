with open(r'.\file\23268.txt') as file:
    data=[list(map(int,i.split()))for i in file]
for pos,line in enumerate(data,start=1):
    pov=[i for i in line if line.count(i)!=1]
    ne_pov = [i for i in line if line.count(i) ==1]
    if sum(pov)/4 < max(ne_pov):
        if len(pov)==4 and len(ne_pov)==3:
            print(pos)
            break