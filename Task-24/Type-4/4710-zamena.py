from string import printable
with open('../files/24_9791.txt') as file:
    data=file.readline().lower()

for i in printable[16:]:
    data=data.replace(i,' ')
data=' '+'0000000000000000000000000000000000000000'+data
while ' 0' in data:
    data=data.replace(' 0',' ')

data=data.split()
print(len(max(data,key=len)))
#ans=0
#for line in data:
 #   line=line.lstrip('0')
#    ans=max(len(line),ans)
#
#print(ans)