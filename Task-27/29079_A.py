from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_A_29079.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='N' and data[2:]=='IV':
            stars.append(dots[-1])
cluster_1=[d for d in dots if d[1]<8]
cluster_2=[d for d in dots if d[1]>8]
stars1=[d for d in stars if d[1]<8]
stars2=[d for d in stars if d[1]>8]
center1=center(cluster_1)
center2=center(cluster_2)
dists=[]
for i in stars1:
    dists.append(dist(i,center2))
for i in stars2:
    dists.append(dist(i,center1))
print(min(dists)*10000,max(dists)*10000)
