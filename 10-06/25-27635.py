from fnmatch import *

for N in range(1230056-1230056%171,10**8+1,171):
    if fnmatch(str(N),f'1*23??56') and N%171==0:
        print(N,N//171)