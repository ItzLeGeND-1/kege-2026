from itertools import combinations
def f(x):
    P= 16<=x<=84
    Q= 27<=x<=43
    A= A1<=x<=A2
    return (A<=P)or Q
lines=[x+eps for x in range(16,85) for eps in (0,0.1,0.9)]
ans=[]
for A1,A2 in combinations(lines,r=2):
    if all(f(x)for x in lines):
        ans.append(A2-A1)
print(max(ans))