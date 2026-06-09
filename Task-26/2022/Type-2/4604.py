with open(r'../../files/26_4604.txt') as file:
    N=int(file.readline())
    boxes=[int(i)for i in file]

boxes=sorted(boxes,reverse=True)

last_boxes=boxes[0]
cnt=1
for box in boxes:
    if last_boxes - box >=3:
        cnt+=1
        last_boxes=box
print(cnt,last_boxes)