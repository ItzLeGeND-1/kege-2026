from math import dist
with open(r'27_B_29077.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data!='VII':
         if int(data[1])<4:
            stars.append(dots[-1])
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]

cl1=[d for d in dots if d[1]>23]
cl2=[d for d in dots if 15<d[1]<23]
cl3=[d for d in dots if d[1]<15]

star1=[d for d in stars if d[1]>23]
star2=[d for d in stars if 15<d[1]<23]
star3=[d for d in stars if d[1]<15]
center3=center(cl3)
print(len(star1),len(star2),len(star3))

