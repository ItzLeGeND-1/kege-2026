from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27A_18677.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
cla1=[d for d in dots if d[1]>(d[0]-8) and d[1]<(d[0]-4)]
cla2=[d for d in dots if d[1]>(d[0]-4) and d[1]<(d[0]+0.7)]
center1=center(cla1)
center2=center(cla2)
#print((center1[0]+center2[0])/2*100000)
#print((center1[1]+center2[1])/2*100000)
with open(r'.\files\27B_18677.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
clusters=[]
eps=1
while dots:
    cluster=[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot,d)<eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster)>5:
        clusters.append(cluster)
centerb1,centerb2,centerb3=(center(cluster)for cluster in clusters)
print((centerb1[0]+centerb2[0]+centerb3[0])/3*100000)
print((centerb1[1]+centerb2[1]+centerb3[1])/3*100000)
