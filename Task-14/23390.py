num=17*125**453+117*5**231-3*5**13-2357
count=0
while num:
    count += num%125 <38
    num//= 125
print(count)