cla0=[];cla1=[]
for n in open('Files/27A_24562.txt'):
    x,y=[float(d)for d in n.replace(',','.').split()]
    if  y>0: cla0+=[(x,y)]
    else: cla1+=[(x,y)]
from math import dist
def centr(cl):
    m=[]
    for d in cl:
        s=sum(dist(d,p)for p in cl)
        m+=[(s,d)]
    return max(m)[1]
x0,y0=centr(cla0)
x1,y1=centr(cla1)
px=min(x0,x1)
py=min(y0,y1)
print(int(abs(x0+x1)*10000),int(abs(y0+y1)*10000))