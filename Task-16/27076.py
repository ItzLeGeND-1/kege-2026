from functools import lru_cache
@lru_cache(None)
def F(n): #2026 - 42
    if n<43: return G(n+4)
    return 2*F(n-2)-F(n-4)+2
@lru_cache(None)
def G(n): # 46 - 11_240
    if n<11240: return G(n+3)+2
    return Q(n)
@lru_cache(None)
def Q(n):#11240 - 20
    if n<21: return n+4
    return Q(n-4)
for i in range(1,11247):
    Q(i)
for i in range(11247,46,-1):
    G(i)
print(F(2026))
#########################################
q=[0]*16000
for n in range(16000):
    if n<21: q[n]=n+4
    else: q[n]=q[n-4]+2
g=[0]*15000
for n in range(15000,1,-1):
    if n<11240: g[n]=g[n+3]+2
    else: g[n]=q[n]
f=[0]*16000
for n in range(15994):
    if n<43: f[n]=g[n+4]
    else: f[n]=2*f[n-2]-f[n-4]+2
print(f[2026])