from turtle import *
screensize(2000,2000)
lt(90)
k=10
tracer(False)

for i in range(5):
    fd(6*k)
    rt(90)
    fd(3*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(2*k)
rt(90)
down()
for i in range(8):
    fd(8*k)
    rt(90)
    fd(5*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(2*k)
lt(90)
down()
for i in range(4):
    fd(5*k)
    lt(90)
up()
for x in range(0,10):
    for y in range(0,10):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()