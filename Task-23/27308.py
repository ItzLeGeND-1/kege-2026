def f(s,e):

    if s==e: return 1
    if s<e: return 0
    return f(s-5,e)+f(s-3,e)+f(s//3,e)
A=f(80,18)*f(18,3)
B=f(80,38)*f(38,3)
AB=f(80,38)*f(38,18)*f(18,3)
print(A+B-AB)