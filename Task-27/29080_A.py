from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_A_29080.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='L' and data[1]=='3':
            stars.append(dots[-1])
cluster_1=[d for d in dots if d[1]<8]
cluster_2=[d for d in dots if d[1]>8]
center1=center(cluster_1)
center2=center(cluster_2)

A1=[]
A2=[]
for i in stars:
    A1.append(dist(center2,i))
for i in stars:
    A2.append(dist(center1,i))
print(max(A1)*10000,max(A2)*10000)
