with open(r'../../files/26_23283.txt') as file:
    K=int(file.readline())
    N=int(file.readline())
    clients=[list(map(int,i.split()))for i in file]
clients=sorted(clients)
window=[0]*K
last_window=0
cnt=0
for client in clients:
    for i in range(K):
        if window[i]<client[0]:
            window[i]=client[1]
            last_window=i+1
            cnt+=1
            break
print(cnt,last_window)
