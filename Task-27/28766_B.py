from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist= sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27_B_28766.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x, y, data= i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='Z' and data[2:]=='I':
            stars.append(list(map(float,[x,y])))
star1=[s for s in stars if s[0]<20 and s[1]<23]
star2=[s for s in stars if s[0]<20 and s[1]>23]
star3=[s for s in stars if s[0]>20]
min_star=[dist(star,star1)for star in stars for star1 in stars]
remove=0.0
while remove in min_star:
    min_star.remove(remove)
print(min(min_star)*10000)
claster1=[s for s in dots if s[0]<20 and s[1]<23]
claster2=[s for s in dots if s[0]<20 and s[1]>23]
claster3=[s for s in dots if s[0]>20]
center1=center(claster1)
center3=center(claster3)
print(dist(center1,center3)*10000)

