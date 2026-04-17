from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]


with open(r'.\files\27_B_17882.txt') as file:
    dots=[list(map(float,i.split())) for i in file]
cla1=[dot for dot in dots if dot[1]>7]
cla2=[dot for dot in dots if dot[0]>5]
cla3=[dot for dot in dots if dot[1]<3]
center1=center(cla1)
center2=center(cla2)
center3=center(cla3)
print((center1[0]+center2[0]+center3[0])/3*10000)
print((center1[1]+center2[1]+center3[1])/3*10000)