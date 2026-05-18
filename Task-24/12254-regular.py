from re import finditer
with open(r'.\files\24_12254.txt') as data:
    data=data.readline()
pattern=r'(RSQ|SQ|Q)(RSQ)+(RSQ|RS|R)'
matches=[match.group()for match in finditer(pattern,data)]
print(len(max(matches,key=len)),max(matches,key=len))