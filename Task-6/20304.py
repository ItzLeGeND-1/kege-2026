from turtle import *
screensize(2000,2000)
tracer(False)
k=20
left(90)
for i in range(9):
    fd(30*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
lt(270)
fd(5*k)
lt(90)
down()
for i in range(2):
    fd(24*k)
    rt(90)
    fd(28*k)
    rt(90)
up()
for x in range(-10,10):
    for y in range(0,33):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()