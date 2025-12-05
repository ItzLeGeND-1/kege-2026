from turtle import *
screensize(2000,2000)
tracer(False)
k=10
lt(90)
for i in range(9):
    fd(27*k)
    rt(90)
    fd(30*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(6*k)
lt(90)
down()
for i in range(9):
    fd(77*k)
    rt(90)
    fd(66*k)
    rt(90)
up()
for x in range(0,25):
    for y in range(0,25):
        goto(x*k,y*k)
        dot(4,'red')
update()
done()
