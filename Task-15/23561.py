def f(x):
    return (x%128==0)<=((x%A!=0)<=(x%80!=0))
for A in range(1,1000):
    if all(f(x)for x in range(1,1000)):
        print(A)