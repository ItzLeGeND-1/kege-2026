from string import printable
from re import finditer
with open(r'.\files\24_23381.txt') as data:
    data=data.readline()
pattern=r'[1-9AB][0-9AB]*[13579B]'
matches=[match.group()for match in finditer(pattern,data)]
print((max(matches)))
print(data.find(''))