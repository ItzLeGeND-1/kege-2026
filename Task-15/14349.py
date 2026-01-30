from itertools import combinations
def f(x):
    B= 54<=x<=120
    C= 78<=x<=151
    A= A1<=x<=A2
    return C<=((B and (not A))<=(not C))
lines=[x+eps for x in range(54,152) for eps in (0,0.1,0.9)]
ans=[]
for A1,A2 in combinations(lines,r=2):
    if all(f(x)for x in lines):
        ans.append(A2-A1)
print(min(ans))
