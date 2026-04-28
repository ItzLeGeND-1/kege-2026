from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist= sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27_B_29076.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='G':
            stars.append(list(map(float,[x,y])))
claster1=[d for d in dots if d[0]>20]
claster2=[d for d in dots if d[0]<20 and d[1]>21]
claster3=[d for d in dots if d[0]<20 and d[1]<21]
stars1=[d for d in stars if d[0]>20]
stars2=[d for d in stars if d[0]<20 and d[1]>21]
stars3=[d for d in stars if d[0]<20 and d[1]<21]
center1=center(claster1)
center2=center(claster2)
center3=center(claster3)
cla1=([dist(center1,star)for star in stars1])
cla2=([dist(center2,star)for star in stars2])
cla3=([dist(center3,star)for star in stars3])
print(max(cla1),max(cla2),max(cla3))