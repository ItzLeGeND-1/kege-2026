from math import dist
def center(claster):
    res=[]
    for dot in claster:
        sum_dot=sum(dist(dot,d)for d in claster)
        res.append([sum_dot,dot])
    return min(res)[1]
#with open(r'.\files\27_A_21599.txt') as file:
    #dots=[list(map(float,i.replace(',','.').split()))for i in file]
#claster1=[dot for dot in dots if dot[1]<-6]
#claster2=[dot for dot in dots if dot[1]>-6 and dot[1]<(10/12*dot[0]-10)]
#claster3=[dot for dot in dots if dot[1]>-6 and dot[1]>(10/12*dot[0]-10)]
#=center(claster1)
#center2=center(claster2)
#center3=center(claster3)
#print((center1[0]+center2[0]+center3[0])/3*10000)
#print((center1[1]+center2[1]+center3[1])/3*10000)
with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
claster1=[dot for dot in dots if dot[1]<-5]
claster2=[dot for dot in dots if -5<dot[1]<dot[0]]
claster3=[dot for dot in dots if dot[0]<dot[1]<(10/7*dot[0]+10)]
claster4=[dot for dot in dots if (10/7*dot[0]+10)<dot[1] and dot[0]>-10]
claster5=[dot for dot in dots if -10>dot[0] and dot[1]<(-19/12*dot[0]-19)]
center1=center(claster1)
center2=center(claster2)
center3=center(claster3)
center4=center(claster4)
center5=center(claster5)
print((center1[0]+center2[0]+center3[0]+center4[0]+center5[0])/5*10000)
print((center1[1]+center2[1]+center3[1]+center4[1]+center5[1])/5*10000)