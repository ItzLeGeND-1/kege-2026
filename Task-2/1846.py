print('a b c d')
for a in 0,1:
    for b in range(2):
        for c in (0,1):
            for d in [0,1]:
                F = (not a and not b) or (b==c) or d
                # все строки истинны
                #if F:
                    #print(a,b,c,d)
                # все строки ложны
                if not F:
                    print(a,b,c,d)
                # строки в перемешку
                #print(a,b,c,d)
