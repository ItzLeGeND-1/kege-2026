from re import finditer

with open(r'..\files\24_4627.txt') as file:
    data=file.readline()

pattern=r'((NP|PN)O)+'
matches=[match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len))/3)
