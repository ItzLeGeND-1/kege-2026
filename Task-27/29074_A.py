from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist= sum(dist(dot,d)for d in cluster)
        res.append([sum_dist,dot])
    return min(res)[1]
with open(r'.\files\27_A_29074.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y, data=i.replace(',','.').split()
        dots.append(list(map(float,[x,y])))
        if data[0]=='Z':
            stars.append(list(map(float, [x, y])))
star1=[s for s in stars if s[1]>10]
star2=[s for s in stars if s[1]<10]
print(len(star1),len(star2))