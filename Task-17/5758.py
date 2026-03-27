with open(r'.\files\17_5758.txt') as file:
    data=[int(i)for i in file]
ans=[]
for i in range(0,len(data)-1):
    for j in range(i+1,len(data)):
        nums=data[i],data[j]
