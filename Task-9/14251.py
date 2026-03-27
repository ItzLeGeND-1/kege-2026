with open(r'.\file\14251.txt') as file:
    data=[list(map(int,i.split()))for i in file]
for pos,line in enumerate(data,start=1):
    pov=[i for i in line if line.count(i)>1]
    ne_pov=[i for i in line if line.count(i)==1]
    neche=[i for i in line if i%2==1]
    if len(pov)==4 and len(ne_pov)==3:
        if sum(pov)<=sum(neche):
            print(sum(line))
            break