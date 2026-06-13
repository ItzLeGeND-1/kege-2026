from math import dist
with open(r'27_A_29077.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data=='N9I':
            stars.append(dots[-1])
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[1]
cl1=[d for d in dots if d[1]>10]
cl2=[d for d in dots if d[1]<10]
st1=[d for d in stars if d[1]>10]
st2=[d for d in stars if d[1]<10]

center1=center(cl1)
center2=center(cl2)
A1=[]
for star in st1:
    A1.append(dist(center1,star))
for star in st1:
    A1.append(dist(center2,star))
print(min(A1)*10000,max(A1)*10000)

