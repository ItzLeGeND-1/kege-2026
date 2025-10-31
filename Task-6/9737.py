from turtle import *
screensize(1000,1000)
tracer(False)
k=20
for i in range(2):
    fd(10*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(7*k)
lt(90)
down()
for i in range(2):
    fd(10*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
for x in range(0,16):
    for y in range(-18,1):
        goto(x*k,y*k)
        dot(5,"red")

update()
done()