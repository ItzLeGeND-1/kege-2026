with open(r'26_17643.txt')as file:
    N=int(file.readline())
    product=[list(map(int,i.split()))for i in file]
product=sorted(product,key=lambda x:(-x[1],x[0],x[2]))



