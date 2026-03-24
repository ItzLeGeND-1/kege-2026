def f(c,e):
    if c==e: return 1
    if c<e or c==13: return 0
    if c>e: return f(c-1,e)+f(c-2,e)+f(c//3,e)
print(f(19,6)*f(6,4))