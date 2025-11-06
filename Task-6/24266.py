from turtle import *
screensize(2000,2000)
tracer(False)
k=20
lt(90)
for i in range(4):

up()
for x in range(-20,20):
    for y in range(0,21):
        goto(x*k,y*k)
        dot(5,"red")

update()
done()