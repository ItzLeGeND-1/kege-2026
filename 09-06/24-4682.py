
with open(r'24_4682.txt') as data:
    data=data.readline()
for i in 'AE':
    data=data.replace(i,'*')
for i in 'BCD':
    data=data.replace(i,'!')
while '**' in data:
    data=data.replace('**','* *')
while '!!' in data:
    data=data.replace('!!','! !')
data=data.split()
print(len(max(data,key=len))//2)