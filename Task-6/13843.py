from turtle import *
screensize(3000,3000)
tracer(False)
k=45
lt(90)
for i in range(5):
    rt(45)
    fd(10*k)
    rt(45)
for i in range(6):
    fd(20*k)
    rt(90)
up()
for x in range(0,20):
    for y in range(-30,10):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()