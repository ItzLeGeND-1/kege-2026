from fnmatch import fnmatch
for N in range(124065-124065%161,10**8+1):
    if fnmatch(str(N),'12*4?65')and N%161:
        print(N,N//161)