from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(8):
    fd(16*k)
    rt(90)
    fd(22*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(8):
    fd(52*k)
    rt(90)
    fd(77*k)
    rt(90)
up()
for x in range(5,25):
    for y in range(5,25):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()
