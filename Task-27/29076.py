from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist= sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27_B_29074.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[1]=='2':
            stars.append(list(map(float,[x,y])))
claster1=[d for d in dots if d[1]>8]
claster2=[d for d in dots if d[1]<8]

stars1=[d for d in stars if d[1]>8]
stars2=[d for d in stars if d[1]<8]

print([len(stars1),len(stars2)])