from math import dist
def center(claster):
    res=[]
    for dot in claster:
        sum_dot=sum(dist(dot,d)for d in claster)
        res.append([sum_dot,dot])
    return min(res)[1]


with open(r'.\files\27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps=2
clusters=[]
while dots:
    cluster=[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d)<eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)
#print([len(cluster)for cluster in clusters])
centers=[center(cluster)for cluster in clusters]
#print(max(center[0]for center in centers)/2*10000)
#print(max(center[1]for center in centers)/2*10000)

with open(r'.\files\27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps=1
clusters=[]
while dots:
    cluster=[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d)<eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster)>1:
       clusters.append(cluster)
max_clusters=centers(max(clusters,key=len))
min_clusters=centers(min(clusters,key=len))
print((max_clusters[0]-min_clusters[0])*10000)
print((max_clusters[1]-min_clusters[1])*10000)