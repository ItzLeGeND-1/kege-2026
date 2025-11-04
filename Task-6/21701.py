from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(2):
    fd(28*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(14*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(30*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
for x in range(0,25):
    for y in range(0,30):
        goto(x*k,y*k)
        dot(5,'red')
update()
done()

