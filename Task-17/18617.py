with open(r'.\files\17_18617.txt') as file:
    data=[int(i)for i in file]
max_3=max(i for i in data)%3
min_7=min(i for i in data)%7
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1= num1%3==max_3
    u2 = num2 % 3 == max_3
    u3= num1%7==min_7
    u4= num2%7==min_7
    if u1+u2>=1 and u3+u4>=1:
        ans.append(num1+num2)
print(len(ans),max(ans))