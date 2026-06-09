with open(r'..\files\26_5988.txt') as file:
    N=int(file.readline())
    boxes=[]
    for line in file:
        size,color = line.split()
        boxes.append((int(size),color))
boxes=sorted(boxes)
max_boxes_by_color={'R':[0,-1],'G':[0,-1],"B":[0,-1]}



