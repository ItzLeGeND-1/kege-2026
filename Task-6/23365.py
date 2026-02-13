from turtle import *
screensize(2000,2000)
tracer(0)
k=10
lt(90)
for i in range(3):
    fd(39*k)
    rt(90)
    fd(48*k)
    rt(90)
up()
fd(27*k)
rt(90)
fd(24*k)
lt(90)
down()
for i in range(3):
    fd(29*k)
    rt(90)
    bk(18*k)
    rt(90)
up()
for x in range(25,43):
    for y in range(0,13):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()

