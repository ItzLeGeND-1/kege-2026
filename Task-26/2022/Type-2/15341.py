with open(r'../../files/26_15341.txt') as file:
    N=int(file.readline())
    breads=[int(i)for i in file]


breads=sorted(breads,reverse=True)
ans=[breads[0]]

for bread in breads:
    if ans[-1]-bread>=8:
        ans.append(bread)

print(len(ans),ans[-1])

