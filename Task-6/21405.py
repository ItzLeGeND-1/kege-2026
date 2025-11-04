from turtle import *
screensize(2000,2000)
tracer(False)
k=30
lt(90)
rt(30)
for i in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)
up()
for x in range(-10,10):
    for y in range(-20,1):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()