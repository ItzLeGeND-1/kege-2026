from turtle import *
screensize(2000,2000)
tracer(False)
k=20
for i in range(5):
    fd(37*k)
    rt(90)
    fd(44*k)
    rt(90)
up()
bk(18*k)
rt(90)
fd(29*k)
lt(90)
down()
for i in range(5):
    fd(31*k)
    rt(90)
    fd(35*k)
    rt(90)
up()
for x in range(21,40):
    for y in range(-18,1):
        goto(x*k,y*k)
        dot(5,"red")

update()
done()