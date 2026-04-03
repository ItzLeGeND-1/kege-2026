
with open(r'.\files\17_2997.txt') as file:
    data=[int(i)for i in file]
nums_3=[int(str(abs(i))[1])for i in data if len(str(abs(i)))==3]
moda=max((nums_3.count(i),i)for i in range(10))[1]
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1= abs(num1)%10==moda
    u2 = abs(num2) % 10 == moda
    if u1+u2>=1:
        ans.append(num1+num2)
print(len(ans),max(ans))
