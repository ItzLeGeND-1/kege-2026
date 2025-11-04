from turtle import *
screensize(2000,2000)
tracer(False)
k=20
for i in range(4):
    fd(19*k)
    rt(90)
    fd(30*k)
    rt(90)
up()
fd(2*k)
rt(90)
fd(8*k)
lt(90)
down()
for i in range(4):
    fd(93*k)
    rt(90)
    fd(97*k)
    rt(90)
up()
for x in range(0,20):
    for y in range(-30,0):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()
