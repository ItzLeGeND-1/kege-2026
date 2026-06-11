with open(r'../../files/26_6031.txt') as file:
    N=int(file.readline())
    rounds=[int(i)for i in file]
rounds=sorted(rounds,reverse=True)

ans=[rounds[0]]
for round in rounds:
    if ans[-1]-round>=6:
        ans.append(round)
print(len(ans),min(ans))