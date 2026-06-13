from math import dist
with open(r'27_B_29081.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[1]>='8':
            stars.append(dots[-1])
cla1=[d for d in dots if d[1]>23]
cla2=[d for d in dots if 15<d[1]<23]
cla3=[d for d in dots if d[1]<15]

stars_1=[d for d in stars if d[1]>23]
stars_2=[d for d in stars if 15<d[1]<23]
stars_3=[d for d in stars if d[1]<15]

B1=[]

for s1 in stars_1:
    for s2 in stars_2:
        B1.append(dist(s1,s2))
for s2 in stars_2:
    for s3 in stars_3:
        B1.append(dist(s2,s3))
for s3 in stars_3:
    for s1 in stars_1:
        B1.append(dist(s1,s3))
print(min(B1)*10000)
B2=[]
for s1 in stars_1:
    for s2 in stars_1:
        if s1!=s2:
            B2.append(dist(s1,s2))
for s1 in stars_2:
    for s2 in stars_2:
        if s1!=s2:
            B2.append(dist(s1,s2))
for s1 in stars_3:
    for s2 in stars_3:
        if s1!=s2:
            B2.append(dist(s1,s2))
print(sum(B2)/len(B2)*10000)