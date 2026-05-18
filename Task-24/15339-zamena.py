with open(r'.\files\24_15339.txt') as data:
    data=data.readline()
for i in 'ABC':
    data=data.replace(i,'*')
for i in '6789':
    data=data.replace(i,'!')
while '**' in data:
    data=data.replace('**','* *')
while '!!' in data:
    data=data.replace('!!','! !')
data=data.split()
print(len(max(data,key=len)))