with open(r'..\files\24_7600.txt') as file:
    data=file.readline()
ans=0
spisok=[]
for a in 'QRS':
    for b in 'QRS':
        spisok.append(a+b)
print(spisok)

for i in range(len(data)-1):
    if data[i:i+2] in spisok:
        cnt=1
        for j in range(i+2,len(data)-1,2):
            if data[j:j+2] in spisok:
                cnt+=1
            else:
                break
        ans=max(ans,cnt)
print(ans)