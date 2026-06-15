from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[-1]
with open(r'27_A_29075.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data!='VII' and data[-3:]=='III':
            stars.append(dots[-1])
cl1=[d for d in dots if d[1]>8]
cl2=[d for d in dots if d[1]<8]

stars1=[d for d in stars if d[1]>8]
stars2=[d for d in stars if d[1]<8]
center1=center(cl1)
center2=center(cl2)
print(center1[0]*10000,center2[1]*10000)