from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_A_29081.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[2:]=='VII':
            stars.append(dots[-1])
cluster_1=[d for d in dots if d[1]<8]
cluster_2=[d for d in dots if d[1]>8]

stars_1=[d for d in stars if d[1]<8]
stars_2=[d for d in stars if d[1]>8]

center_1=center(cluster_1)
center_2=center(cluster_2)

dists=[]
for s in stars_1:
    dists.append(dist(center_1,s))
for s in stars_2:
    dists.append(dist(center_2,s))
print(min(dists)*10000,max(dists)*10000)