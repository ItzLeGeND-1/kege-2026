from turtle import *
screensize(2000,2000)
tracer(0)
lt(90)
k=10
for i in range(4):
    fd(10*k)
    rt(270)
up()
fd(3*k)
rt(270)
fd(5*k)
rt(90)
down()
for i in range(2):
    fd(10*k)
    rt(270)
    fd(12*k)
    rt(270)
up()
for x in range(-10,10):
    for y in range(-10,11):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()