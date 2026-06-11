with open(r'../../files/26_17565.txt') as file:
    N,S=map(int,file.readline().split())
    matross=[list(map(int,i.split()))for i in file]
matross=sorted(matross,key=lambda x:(x[1]+x[2]+x[3],x[4],-x[0]),reverse=True)
ans=[]
for matros in matross:
    if len(ans)<S:
        ans.append([matros[0],matros[1]+matros[2]+matros[3]])
print(ans)
ans1=[]
for matros1 in matross:
    ans1.append([matros1[1]+matros1[2]+matros1[3]])
print(ans1)