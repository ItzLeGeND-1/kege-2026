from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
rt(270)
for i in range(2):
    fd(8*k)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3*k)
    rt(240)
rt(240)
for i in range(2):
    fd(14*k)
    rt(120)
up()
for x in range(-20,20):
    for y in range(0,21):
        goto(x*k,y*k)
        dot(5,"red")

update()
done()