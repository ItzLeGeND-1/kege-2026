def f(x):
    P= x in range(2,21,2)
    Q= x in range(3,31,3)
    A= x in As
    return (A<=P) and ((not Q)<= (not A))
As=[]
for x in range(1,100):
    if not f(x):
        As.append(x)
