from functools import lru_cache
@lru_cache(None)
def g(n):
    if n>=248045: return n/20+28
    return g(n+9)-4
for i in range(250000,10,-1):
    g(i)


def f(n):
    if n>=19: return f(n-4)+3580
    return 6*(g(n-7)-36)


print(f(673))
