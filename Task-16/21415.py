from sys import setrecursionlimit
def F(n):
    if n<=5: return 1
    return n+F(n-2)
setrecursionlimit(2128//2)
print(F(2126)-F(2122))

###############################################################################

f=[0]*2200
for i in range(2200):
    if i<=5: f[i]=1
    else: f[i]=i+f[i-2]
print(f[2126]-f[2122])