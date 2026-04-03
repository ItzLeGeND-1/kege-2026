with open(r'.\files\26.2_19727.txt') as file:
    M,N=map(int,file.readline().split())
    bidons=[int(i)for i in file]
bidons=sorted(bidons)
ans=[]
for bidon in bidons:
    if sum(ans)+bidon<=M:
        ans.append(bidon)
free_space=M-sum(ans[:-1])
print(len(ans),len([i for i in bidons if i > free_space]))