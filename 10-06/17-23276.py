with open(r'17_23276.txt') as file:
    data=[int(i)for i in file]
max_25=max(i for i in data if i%100==25)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1= 999<abs(num1)<10000
    u2 = 999 < abs(num2) < 10000
    u3 = 999 < abs(num3) < 10000
    if u1+u2+u3<=2 and num1+num2+num3<=max_25:
        ans.append(num1+num2+num3)
print(len(ans),max(ans))
