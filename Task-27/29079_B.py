from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]
with open(r'.\files\27_B_29079.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='J' and data[2:]=='V':
            stars.append(dots[-1])
claster1=[d for d in dots if d[0]>20]
claster2=[d for d in dots if d[0]<20 and d[1]>21]
claster3=[d for d in dots if d[0]<20 and d[1]<21]
stars1=[d for d in stars if d[0]>20]
stars2=[d for d in stars if d[0]<20 and d[1]>21]
stars3=[d for d in stars if d[0]<20 and d[1]<21]
print(len(claster1),len(claster2),len(claster3))
print(max(stars1)[0]*10000,max(stars2,key=lambda x:x[1])[1]*10000)
