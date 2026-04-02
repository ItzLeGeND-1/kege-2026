from sys import setrecursionlimit
setrecursionlimit(1000000)
def F(n):
    return 3*(G(n-2)+5)

def G(n):
    if n<8: return 3*n
    return G(n-3)

print(F(12345))