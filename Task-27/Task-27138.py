from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27A_27138.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
cla1=[d for d in dots if d[0]>0]
cla2=[d for d in dots if d[0]<0]
cn1=center(cla1)
cn2=center(cla2)
print(abs(cn1[0]-cn2[0])*10000)
print(abs(cn1[1]-cn2[1])*10000)
with open(r'.\files\27B_27138.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
clab1=[d for d in dots if d[0]>0 and d[1]<-20]
clab2=[d for d in dots if d[0]>0 and d[1]>10]
clab3=[d for d in dots if d[0]<-25]
maxx_x=max(x for x in clab3)
print(abs(maxx_x[0])*10000)
def distclaster(cla1,cla2,cla3):
    res=[]
    for dot1 in cla1:
        sum_dist=sum(dist(dot1,dot2)for dot2 in cla2)+sum(dist(dot1,dot3)for dot3 in cla3)
        res.append([sum_dist,dot1])
    return max(res)
print(distclaster(clab1,clab2,clab3))
print(distclaster(clab2,clab1,clab3))
print(distclaster(clab3,clab2,clab1))