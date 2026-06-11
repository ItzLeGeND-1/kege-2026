with open(r'../../files/26_17537.txt') as file:
    N,M,K=map(int,file.readline().split())
    places=[list(map(int,i.split()))for i in file]

seats=[M]*(K+1)
for row,seat in places:
    seats[seat]=min(seats[seat],row-1)
ans=[]
for i in range(1,K):
    ans.append([min(seats[i],seats[i+1]),i+1])
print(max(ans))