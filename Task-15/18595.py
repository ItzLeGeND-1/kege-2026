from itertools import combinations

def f(x):
    C= 48<=x<=94
    J= 83<=x<=100
    A= A1<=x<=A2
    return (not(C or J))<=(not A)
line_A=[48,94,83,100]
line_x=[49,87,95]
#line=[x+eps for x in range(48,101) for eps in (0,0.1,0.9)]
ans=[]
for A1,A2 in combinations(line_A,2):
    if all(f(x)for x in line_x):
        ans.append(A2-A1)
print(max(ans))