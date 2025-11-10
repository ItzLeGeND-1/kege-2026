from turtle import *
screensize(3000,3000)
tracer(False)
k=45
lt(90)
up()
for i in range(10):
    rt(120)
    fd(10*k)
down()
for i in range(7):
    fd(15*k)
    rt(90)
for i in range(5):
    rt(60)
    fd(20*k)
    rt(30)
up()
for x in range(0,20):
    for y in range(-30,1):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()