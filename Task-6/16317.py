from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(2):
    fd(21*k)
    rt(90)
    fd(27*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(86*k)
    rt(90)
    fd(47*k)
    rt(90)
up()
for x in range(10,30):
    for y in range(9,25):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()