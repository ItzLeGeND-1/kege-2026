from math import *
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27.21.A_19715 (1).txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
eps=1
clusters=[]
while dots:
    cluster=[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d)<eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster)>7:
       clusters.append(cluster)
centers=[center(cluster)for cluster in clusters]
print(sum(c[0]for c in centers)/len(centers)*10000)
print(sum(c[1]for c in centers)/len(centers)*10000)