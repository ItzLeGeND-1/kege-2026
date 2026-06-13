with open(r'../../files/26_2_23175.txt') as file:
    N,M=map(int,file.readline().split())
    loads=[int(file.readline())for i in range(N)]
    containers=[int(file.readline())for i in range(M)]

loads=sorted(loads)
containers=sorted(containers)
loaded=[]
last_container=0
for load in loads:
    for container in containers.copy():
        if load<=container:
            loaded.append(load)
            last_container=container
            containers.remove(container)
            break
loaded=loaded[:-1]
for load in loads[::-1]:
    if last_container-load>=0:
        loaded.append(load)
        break
print(len(loaded),loaded[-1]-loaded[-2])
