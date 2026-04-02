from itertools import product,permutations
def f(x,y,z,w):
    return ((z==x)<=w)and(w<=(y and x))
for a,b,c in product([0,1],repeat=3):
    tab=[(1,1,a,0),
         (1,b,c,0),
         (1,0,1,1)]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t)))for t in tab]==[1,1,1]:
                print(*p)