from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(2):
    fd(23*k)
    lt(90)
    bk(27*k)
    lt(90)
up()
bk(5*k)
rt(90)
fd(11*k)
lt(90)
down()
for i in range(2):
    fd(26*k)
    rt(90)
    fd(32*k)
    rt(90)
up()
for x in range(1,30):
    for y in range(-5,25):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()