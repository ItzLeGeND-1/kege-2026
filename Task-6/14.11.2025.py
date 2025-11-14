from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(9):
    fd(22*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(9):
    fd(53*k)
    rt(90)
    fd(75*k)
    rt(90)
up()
for x in range(-10,10):
    for y in range(-10,30):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()
