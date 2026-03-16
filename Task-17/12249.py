with open(r'.\files\17_12249.txt') as file:
    data=[int(i)for i in file]
max_3=max(i for i in data if str(i)[-1]=='3' and 10000<=i<=99999)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=(str(num1))[-1]=='3'
    u2 = (str(num2))[-1] == '3'
    u3 = (str(num3))[-1] == '3'
    summ=num1+num2+num3
    if u1+u2+u3>=1 and summ<=max_3:
        ans.append(num1+num2+num3)
print(len(ans),max(ans))
