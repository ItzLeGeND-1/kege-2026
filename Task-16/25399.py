from sys import setrecursionlimit
setrecursionlimit(100000)
def g(n):
    if n>303728: return n-15
    return g(n+8)/2-109

def f(n):
    if n>=128: return f(n-5)+1092
    return 5*g(n-7)+29


print(f(2049))