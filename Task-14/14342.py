from string import printable

for p in range(25,36):
    num1=int(f'BO',p)
    num2=int(f'OM',p)
    num3=int(f'BL4',p)
    num4=int(f'CNG',p)
    if num1+num2+num3==num4:
        print(p)