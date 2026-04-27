from math import dist
def center(claster):
    res=[]
    for dot in claster:
        sum_dot=sum(dist(dot,d)for d in claster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_A_17915.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
claster1=[dot for dot in dots if dot[0]<6 and dot[1]>20]
claster2=[dot for dot in dots if dot[0]>6 and dot[1]>23]
claster3=[dot for dot in dots if dot[0]>6 and dot[1]<23]
center1=center(claster1)
center2=center(claster2)
center3=center(claster3)
print((center1[0]+center2[0]+center3[0])/3*10000)
print((center1[1]+center2[1]+center3[1])/3*10000)