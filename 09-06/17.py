with open(r'17_23376.txt') as file:
    data=[int(i)for i in file]
max_37=max(i for i in data if i%100==37 and 9999<i<100000)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1= 9999<abs(num1)<100000
    u2 = 9999 < abs(num2) < 100000
    if (num1+num2)**2>max_37**2 and u1+u2==1:
        ans.append(num1+num2)
print(len(ans),max(ans))
