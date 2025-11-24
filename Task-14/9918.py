from string import printable
o=[]
for x in range(1,66):
    for y in range(1,x-1):
        num1=int(f'73{printable[x]}1{printable[y]}',67)
        num2=int(f'49{printable[y]}6',x)
        num=num1+num2
        o+=[num,num//(x+y)]
print(o)