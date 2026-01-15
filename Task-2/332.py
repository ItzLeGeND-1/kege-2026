from itertools import product,permutations
def f(x,y,z,w):
    return (x or y and (not z))and (not w)
tab=[(1,0,0,0,1),(0,0,1,0,1),(0,1,0,1,0)]
for p in permutations('xyzw'):
    if all(f(**dict(zip(p,t)))==t[-1] for t in tab):
        print(*p)

