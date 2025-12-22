from re import *

with open(r'.\files\24_25361.txt')as file:
    data=file.readline()

pattern=r''
matches=[match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)))