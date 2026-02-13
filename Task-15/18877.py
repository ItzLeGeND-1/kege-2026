def f(x,y):
    return ((x<7)or(y>=5*x+A-60)or(x>=36)or(y<225))
for A in range(0,1000):
    if all(f(x,y)for x in range(0,1000) for y in range(0,1000)):
        print(A)