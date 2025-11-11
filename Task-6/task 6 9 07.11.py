from turtle import *
tracer(False)
screensize(2000,2000)
k=20
lt(90)
for i in range(2):
    fd(20*k)
    lt(270)
    fd(12*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(7*k)
lt(90)
down()
for i in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
for x in range(0,20):
    for y in range(0,30):
        goto(x*k,y*k)
        dot(5,'red')

update()
done()