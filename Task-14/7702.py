from string import printable
o=[]
for y in range(9,18):
    for x in range(0,y):
        num1=int(f'5{printable[x]}{printable[y]}A',18)
        num2=int(f'18{printable[x]}7',y)
        num=num1+num2
        o+=[num]
print(len(set(o)))

