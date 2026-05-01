from math import dist
def center(claster):
    res=[]
    for dot in claster:
        sum_dot=sum(dist(dot,d)for d in claster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_B_17915.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
claster1=[dot for dot in dots if dot[0]<12 and dot[1]>15]
claster2=[dot for dot in dots if dot[0]>15 and dot[1]<10]
claster3=[dot for dot in dots if dot[0]<15 and dot[1]<10]
claster4=[dot for dot in dots if dot[0]>22 and dot[1]>15]
center1=center(claster1)
center2=center(claster2)
center3=center(claster3)
center4=center(claster4)
print((center1[0]+center2[0]+center3[0]+center4[0])/4*10000)
print((center1[1]+center2[1]+center3[1]+center4[1])/4*10000)