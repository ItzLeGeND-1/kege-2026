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
        x,y, data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='L' and data[-1:]=='V':
            stars.append(list(map(float, [x, y])))
claster1=[d for d in dots if d[0]>20]
claster2=[d for d in dots if d[0]<20 and d[1]<22]
claster3=[d for d in dots if d[0]<20 and d[1]>22]
star1=[d for d in stars if d[0]>20]
star2=[d for d in stars if d[0]<20 and d[1]<22]
star3=[d for d in stars if d[0]<20 and d[1]>22]
center1=center(claster1)
center2=center(claster2)
center3=center(claster3)
ans=[]
ans.append(min(dist(center1,s)for s in star1))
ans.append(min(dist(center2,s)for s in star2))
ans.append(min(dist(center3,s)for s in star3))
ans.append(max(dist(center1,s)for s in star1))
ans.append(max(dist(center2,s)for s in star2))
ans.append(max(dist(center3,s)for s in star3))
print(min(ans)*10000,max(ans)*10000)