with open(r'./files/26_17643.txt') as file:
    N=int(file.readline())
    data=[list(map(int,i.split()))for i in file]
middle=sum(i[1]for i in data)/N
goods={}

for ID,price,status in data:
    if price>middle:
        if ID not in goods:
            goods[ID]=[not status,price,status]
        else:
            goods[ID][2]+=status
            goods[ID][0]+=(not status)

goods1=sorted(goods,key=lambda x: (goods[x][0],goods[x][1],-goods[x][2]))
print(goods[goods1[-1]],51*856)


