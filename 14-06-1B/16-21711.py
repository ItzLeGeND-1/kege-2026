def f(n):
    if n<47800: return n
    return (n-6)*f(n-7)
print((f(47872)-290*f(47865))/f(47858))