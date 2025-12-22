from turtle import *
screensize(2000,2000)
tracer(False)
lt(90)
k=20
for n in range(6):
    fd(33*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(9*k)
lt(90)
down()
for n in range(6):
    fd(24*k)
    rt(90)
    fd(25*k)
    rt(90)
up()
for x in range(1,30):
    for y in range(1,30):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()