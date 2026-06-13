with open(r'../../files/26_17881.txt') as file:
    N=int(file.readline())
    students=[list(map(int,i.split()))for i in file]
students=sorted(students,key=lambda x:(-(x[1]+x[2]+x[3]+x[4]),x[0]))
ans=[]
K=0
for student in students:
    if student.count(2)==0:
        ans.append(student)
        K+=1
    if K==N//4:
        break

ans2=[]
for student in students:
    if student.count(2)>2:
        ans2.append(student)
print(min(ans,key=lambda x: (x[1]+x[2]+x[3]+x[4],-x[0])),max(ans2,key=lambda x:(x[1]+x[2]+x[3]+x[4],-x[0])))