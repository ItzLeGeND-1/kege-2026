with open(r'.\files\17_6791.txt') as file:
    data=[int(i)for i in file]
min_68=(min(i for i in data if abs(i)%100==68))**2
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1= abs(num1)%100==68
    u2 = abs(num2)%100==68
    summ=num1**2+num2**2
    if summ>=min_68 and u1+u2==1:
        ans.append(num1**2+num2**2)
print(len(ans),max(ans))