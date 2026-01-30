from itertools import combinations


def f(x):
    B= 70<=x<=90
    A= 0<A1<=x<=A2
    return (x%A==0)or(B<=(not(x%22==0)))
line_a=[70,90]
line_x=[71]
ans=[]
for A1,A2 in combinations(line_a,2):
    if all(f(x) for x in line_x):
        ans.append(A1)
print(ans)