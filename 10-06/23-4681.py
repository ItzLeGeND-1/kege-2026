def f(s,e):
    if s==e: return 1
    if s>e: return 0
    return f(s+3,e)+f(s*2,e)
print(f(3,27)*f(27,63))