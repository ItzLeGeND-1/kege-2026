from turtle import *
screensize(2000,2000)
tracer(False)
k=40
left(90)
rt(90)
for i in range(7):
    rt(45)
    fd(11*k)
    rt(45)
up()
for x in range(-10,10):
    for y in range(-20,10):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()