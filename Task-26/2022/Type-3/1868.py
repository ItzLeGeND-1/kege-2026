with open(r'../../files/26_1868.txt') as file:
    N=int(file.readline())
    places=[list(map(int,i.split()))for i in file]

places=sorted(places,key=lambda x:(-x[0],x[1]))
ans=[]
for num1,num2 in zip(places,places[1:]):
    if num1[0]==num2[0]:
      if abs(num1[1]-num2[1])==3:
        ans.append(num1)
print(ans[0][0],ans[0][1]+1)