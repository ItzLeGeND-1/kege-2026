from math import dist
def center(cluster):
    res=[]
    for dot in cluster:
        sum_dot=sum(dist(dot,d)for d in cluster)
        res.append([sum_dot,dot])
    return min(res)[-1]
with open(r'27_B_29075.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data!='VII' and data[0]=='J':
            stars.append(dots[-1])
cl1=[d for d in dots if d[1]>23]
cl2=[d for d in dots if d[1]<23 and d[0]<20]
cl3=[d for d in dots if d[1]<23 and d[0]>20]

stars1=[d for d in stars if d[1]>23]
stars2=[d for d in stars if d[1]<23 and d[0]<20]
stars3=[d for d in stars if d[1]<23 and d[0]>20]

B1=[]
for star1 in stars1:
    for star2 in stars2:
        B1.append(dist(star1,star2))
for star1 in stars1:
    for star3 in stars3:
        B1.append(dist(star1,star3))
for star3 in stars3:
    for star2 in stars2:
        B1.append(dist(star3,star2))
print(min(B1)*10000,max(B1)*10000)