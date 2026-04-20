from math import dist
with open(r'.\files\27_A_23209.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
def center(claster):
    res=[]
    for dot in claster:
        sum_dist=sum(dist(dot,d)for d in claster)
        res.append([sum_dist,dot])
    return min(res)[1]
claster_A1=[d for d in dots if d[0]<5]
claster_A2=[d for d in dots if d[0]>5]
with open(r'.\files\27_B_23209.txt') as file:
    dots=[list(map(float,i.replace(',','.').split()))for i in file]
cla1=[d for d in dots if 15<d[1]<21 and 5<d[0]<15]
cla2=[d for d in dots if d[1]>21 and 5<d[0]<15]
cla3=[d for d in dots if d[1]<15 and 5<d[0]<15]

cluster_B=[cla1,cla2,cla3]

max_center=center(max(cluster_B,key=len))
min_center=center(max(cluster_B,key=len))

center_B1_x,center_B1_y=(center(cla1))
center_B2_x,center_B2_y=(center(cla2))
center_B3_x,center_B3_y=(center(cla3))

cla_ob_x=[(len(cla1),center_B1_x),(len(cla2),center_B2_x),(len(cla3),center_B3_x)]
cla_ob_y=[(len(cla1),center_B1_y),(len(cla2),center_B2_y),(len(cla3),center_B3_y)]

print((max(cla_ob_x)[1]-min(cla_ob_x)[1])*10000)
print(abs(max(cla_ob_y)[1]-min(cla_ob_y)[1])*10000)

