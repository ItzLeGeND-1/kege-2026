with open(r'../../files/26_12256.txt')as file:
    S,N=map(int,file.readline().split())
    conts=[int(i)for i in file]


conts=sorted(conts)
track=[]
for cont in conts:
    if sum(track)+cont<=S:
        track.append(cont)
    if sum(track[:-1])+cont<S:
        track[-1]=cont
print(len(track),max(track))
