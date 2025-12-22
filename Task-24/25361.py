with open(r'.\files\24_25361.txt') as data:
    data=data.readline()
ans=0
for i in range(len(data)):
    if data[i] in '02468':
        cnt_F=0
        cnt=1
        for j in range(i+1, len(data)):
            if data[j]=='F':
                cnt_F+=1
            if cnt_F==77 or data[j] in '02468':
                break
            cnt += 1
        if cnt_F in [76 , 77] :
            ans=max(ans,cnt)
print(ans)