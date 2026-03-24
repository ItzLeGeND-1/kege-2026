from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)

for i in range(2):
    fd(14*k)
    lt(270)
    bk(12*k)
    rt(90)
up()
fd(9*k)
rt(90)
bk(7*k)
lt(90)
down()
for i in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
for x in range(-10,10):
    for y in range(8,20):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()