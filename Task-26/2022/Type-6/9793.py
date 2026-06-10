with open(r'../../files/26_9793.txt') as file:
    N=int(file.readline())
    details=[list(map(int,i.split()))for i in file]

details=sorted(details,key=lambda x:(x[0],x[1]))
print(max(details))



