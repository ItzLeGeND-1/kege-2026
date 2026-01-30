from itertools import combinations
def f(x):
    Q= 25<=x<=42
    P= 1<=x<=98
    A= A1<=x<=A2
    return Q<=(((not P)and Q) <= A)
line_A=[1,25,42,98]
line_x=[2,26,43]
ans=[]
for A1,A2 in combinations(line_A,2):
    if all(f(x) for x in line_x):
        ans.append(A2-A1)
print(min(ans))
