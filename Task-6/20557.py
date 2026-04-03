from turtle import *
screensize(2000,2000)
tracer(False)
lt(90)
k=10
for i in range(4):
    fd(36*k)
    rt(90)
    fd(41*k)
    rt(90)
up()
rt(90)
fd(20*k)
lt(90)
fd(20*k)
down()
for i in range(4):
    fd(25*k)
    rt(90)
up()
fd(7*k)
lt(90)
fd(7*k)
rt(90)
down()
for i in range(7):
    fd(16*k)
    rt(90)
up()
for x in range(20,30):
    for y in range(27,37):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()
