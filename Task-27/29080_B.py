from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_B_29080.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='L':
            stars.append(dots[-1])
stars_1=[d for d in stars if 23<d[1]]
stars_2=[d for d in stars if 16<d[1]<23]
stars_3=[d for d in stars if d[1]<16]
claster_1=[d for d in dots if 23<d[1]]
claster_2=[d for d in dots if 16<d[1]<23]
claster_3=[d for d in dots if d[1]<16]
print(len(stars_1),len(stars_2),len(stars_3))
center1=center(claster_1)
center3=center(claster_3)
print(dist(center1,center3)*10000)
B2=[]
for i in stars:
    for q in stars:
        B2.append(dist(i,q))
print(max(B2)*10000)

