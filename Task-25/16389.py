from fnmatch import fnmatch
for N in range(5023030-5023030%98591,10**10+1,98591):
    if fnmatch(str(N),'5?2*3?3?')and N%98591==0:
        print(N,N//98591)