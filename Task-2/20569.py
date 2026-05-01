from itertools import product,permutations
def f(x,y,z,w):
    return ((w<=z)==(x<=(not y)))and (x or z)
for a,b in product([0,1],repeat=2):
    tab=[(1,0,0,1),
         (1,1,1,0),
         (0,a,0,b)]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t)))for t in tab]==[1,0,1]:
                print(*p)