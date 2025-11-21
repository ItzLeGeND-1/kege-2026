from turtle import *
screensize(10000,10000)
tracer(False)
k=20
lt(90)
rt(45)
for i in range(10):
    rt(45)
    fd(203*k)
    rt(45)
up()
bk(40*k)
rt(45)
down()
for i in range(5):
    fd(20*k)
    lt(90)
up()
for x in range(200,300):
    for y in range(-300,-100):
        goto(x*k,y*k)
        dot(2,'red')
update()
done()
