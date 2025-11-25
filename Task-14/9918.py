from string import printable
o=set()
for x in range(10,67):
    for y in range(0,x):
        num1=7*67**4 + 3*67**3 + x*67**2 + 1*67**1 + y
        num2=4*67**3 + 9*67**2 + y*67**1 + 6
        num=num1+num2
        o.add(num)
print(len(set(o)))