from itertools import combinations

def f(x):
    P= [2,4,6,8,10,12,14,16,18,20]
    Q=[3,6,9,12,15,18,21,24,27,30]
    R=[12,24,36,48,60]
    A=A1<=x<=A2
    return (not A)<=((P and Q)<=R)
lines=[x+eps for x in range(2,61) for eps in(0,0.1,0,9)]
ans=[]
for A1,A2 in combinations(lines,2):
    if all(f(x) for x in lines):
        ans.append(A2-A1)
print(min(ans))