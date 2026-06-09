with open(r'../../files/26_3586.txt') as file:
    N=int(file.readline())
    trees = [list(map(int, i.split())) for i in file]

trees=sorted(trees,key=lambda x:(-x[0],x[1]))
ans=[]
dlina=0
for tree1,tree2 in zip(trees,trees[1:]):
    if tree1[0] == tree2[0]:
        if tree2[1]-tree1[1]>dlina:
            dlina=tree2[1]-tree1[1]

for tree1,tree2 in zip(trees,trees[1:]):
    if tree1[0] == tree2[0]:
        if tree2[1]-tree1[1]==dlina:
            ans.append(tree2[0])
print(max(ans),dlina-1)
