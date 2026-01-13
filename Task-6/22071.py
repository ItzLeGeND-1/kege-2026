from turtle import *
screensize(2000,2000)
tracer(False)
k=10
lt(90)

fd(30*k)
lt(60)
fd(24*k)
rt(240)
fd(54*k)
lt(120)
fd(24*k)
lt(60)
up()
fd(30*k)
rt(90)
fd(20*k)
lt(90)
down()
for i in range(17):
    fd(6*k)
    lt(90)
    fd(80*k)
    lt(90)
up()
for x in range(-30,10):
    for y in range(30,38):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()
