def f(x):
    B= 50<=x<=70
    return (x%A==0) or (B<=(x%16!=0))
for A in range(1,1000):
    if all(f(x)for x in range(1,1000)):
        print(A)