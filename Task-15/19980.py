from itertools import combinations
def f(x):
    P = 52<=x<=105
    Q= 0<=x<=53
    A= A1<=x<=A2
    return ((not P) and( not Q) and (not A))<=((x**2)>303601)
lines=[x+eps for x in range(0,106) for eps in (0,0.1,0.9)]
ans=[]
for A1,A2 in combinations(lines,2):
    if all(f(x)for x in lines):
        ans.append(A2-A1)
print(min(ans))