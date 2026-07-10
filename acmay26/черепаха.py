from turtle import *
from math import sin, pi

shape('turtle')
colormode(255)
color((49, 235, 49))
ln = 200
penup()
goto(0, -200)
pendown()
for n in range(3):
    begin_fill()
    fd(ln / 2)
    for i in range(3):
        lt(120)
        forward(ln)
    backward(ln / 2)
    end_fill()
    lt(90)
    h = ln * sin(pi * 60 / 180)
    fd(h - 40)
    rt(90)
    ln -= 40
mainloop()
