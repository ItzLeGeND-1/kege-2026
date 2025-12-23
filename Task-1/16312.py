from itertools import permutations

graph='AG GD DB FB EF DE CD AC AD'.split()
matrix='37 57 147 37 26 57 12346'.split()
print(*range(1,9))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1)in matrix[i.index(y)]for x,y in graph):
        print(*i)