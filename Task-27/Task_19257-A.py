from math import dist
def center(claster):
    res=[]
    for dot in claster:
        sum_dist=sum(dist(dot,d)for d in claster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27_A_19257.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
cla1=[dot for dot in dots if dot[1]>5]
cla2=[dot for dot in dots if dot[1]<5]
center1=center(cla1)
center2=center(cla2)
print(abs((center1[0]+center2[0])/2*10000))
print(abs(center1[1]+center2[1])/2*10000)
