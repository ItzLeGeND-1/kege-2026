with open(r'26_20910.txt') as file:
    N=file.readline()
    bilets=[list(map(int,i.split()))for i in file]
bilets=sorted(bilets,key=lambda x:(-x[0],x[1]))
ans=[]
for num1,num2 in zip(bilets,bilets[1:]):
    if num1==num2:
        if
