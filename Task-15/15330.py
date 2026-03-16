from itertools import combinations
def f(x):
    B= 24<=x<=90
    C= 47<=x<=115
    A= A1<=x<=A2
    return C<=((not A and B)<=(not C))
line=[x+eps for x in range(24,116) for eps in (0,0.1,0.9)]
ans=[]
for A1,A2 in combinations(line,r=2):
    if all(f(x)for x in line):
        ans.append(A2-A1)
print(min(ans))
