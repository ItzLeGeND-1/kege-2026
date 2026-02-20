for p in range(11,37):
    for x in range(1,500001):
        num1=int(f'29A1',p)
        num2 = int(f'47771', p)
        num3 = int(f'12A', p)
        if num1+num2+num3==1000000+x:
            print(p)
