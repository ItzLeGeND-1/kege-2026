def f(x,e):
    if x==e: return 1
    if x>e or x==10: return 0
    return f(x+1,e)+f(x+2,e)+f(x*2,e)
print(f(3,7)*f(7,20))