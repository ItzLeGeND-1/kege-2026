from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist= sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27_A_29076.txt') as file:
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

center1=center(claster1)
center2=center(claster2)
print(center1[0]*10000)
print(center2[1]*10000)