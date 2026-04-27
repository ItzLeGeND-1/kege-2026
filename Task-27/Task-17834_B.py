from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist=sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]


with open(r'.\files\27_B_17834.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]
claster1=[dot for dot in dots if dot[0]<4 and dot[1]>2]
claster2=[dot for dot in dots if  dot[1]<2]
claster3=[dot for dot in dots if dot[0]>4 and dot[1]>2]
center1=center(claster1)
center2=center(claster2)
center3=center(claster3)
print((center1[0]+center2[0]+center3[0])/3*100)
print((center1[1]+center2[1]+center3[1])/3*100)