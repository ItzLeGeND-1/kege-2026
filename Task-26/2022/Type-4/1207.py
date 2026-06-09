with open(r'../../files/26_1207.txt') as file:
    S,N=map(int,file.readline().split())
    files=[int(i)for i in file]
files=sorted(files)

disk=[]
for file in files:
    if sum(disk)+file<S:
        disk.append(file)
    if sum(disk[:-1])+file<=S:
        disk1=disk.pop()
        disk.append(file)
print(len(disk),max(disk))