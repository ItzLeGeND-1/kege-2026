with open(r'26_16335.txt') as file:
    N=int(file.readline())
    breads=[int(i)for i in file]

breads=sorted(breads,reverse=True)

ans=[breads[0]]

for bread in breads:
    if ans[-1]-bread>=4:
        ans.append(bread)
print(len(ans),min(ans))