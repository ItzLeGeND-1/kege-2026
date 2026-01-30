def f(x):
    return x%A==0 or ((x%133==0)<=(x%95!=0))
for A in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(A)