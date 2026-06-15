from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[-1]
with open('27_B_29074.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='L' and data[-1]=='V':
            stars.append(dots[-1])
cl1=[d for d in dots if d[1]>23]
cl2=[d for d in dots if d[1]<23 and d[0]<20]
cl3=[d for d in dots if d[1]<23 and d[0]>20]

stars1=[d for d in stars if d[1]>23]
stars2=[d for d in stars if d[1]<23 and d[0]<20]
stars3=[d for d in stars if d[1]<23 and d[0]>20]

center1=center(cl1)
center2=center(cl2)
center3=center(cl3)
B1=[]
for star in stars1:
    B1.append(dist(center1,star))
for star in stars2:
    B1.append(dist(center2,star))
for star in stars3:
    B1.append(dist(center3,star))
print(min(B1)*10000,max(B1)*10000)