with open(r'.\files\24_1273.txt') as data:
    data=data.readline()

data=data.replace("XYZ","XY YZ")
data=data.split()
print(len(max(data,key=len)))

"PRIVE RIVET"