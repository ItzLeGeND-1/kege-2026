from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(2):
    fd(5*k)
    lt(90)
    bk(13*k)
    lt(90)
up()
bk(10*k)
rt(90)
fd(9*k)
lt(90)
down()
for i in range(2):
    fd(11*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
for x in range(0,20):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()

