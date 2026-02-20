from functools import lru_cache
@lru_cache(None)
def F(n):
    if n==1:
        return 1
    return (n+1)*F(n-1)
for i in range(2,2030)