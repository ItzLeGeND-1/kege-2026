from itertools import product,permutations

def f(x,y,z,w):
    return not(y<=(x==z))and(w<=x)
for a,b,c,d,e,g,h in product([0,1],repeat=7):
    tab=[(a,0,0,b),
         (0,c,0,d),
         (e,1,g,h)]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t)))for t in tab]==[1,1,1]:
                print(*p)

