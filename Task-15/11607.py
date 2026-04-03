def f(x):
    return not(not((x%263==0)<=(x%A==0)) and (x%71==0))
for A in range(1,100_000):
    if all(f(x)for x in range(1,20_000)[::-1]):
        print(A)