import turtle
import random
from time import sleep

bug = turtle.Turtle()
bug.color('#3f878e','#3f878e')
bug.pensize(5)
bug.shape('turtle')
bug.penup()
bug.goto(300,60)
bug.pendown()
bug.circle(40)
bug.penup()
bug.goto(-400,100)
bug.pendown()
bug.right(0)

elseif = turtle.Turtle()
elseif.color('#7fbd01','#7fbd01')
elseif.pensize(5)
elseif.shape('turtle')
elseif.penup()
elseif.goto(300,-140)
elseif.pendown()
elseif.circle(40)
elseif.penup()
elseif.goto(-400,-100)
elseif.pendown()
elseif.right(0)

while True:
    bug.forward(random.randrange(1,10))
    elseif.forward(random.randrange(1,10)) 

    if bug.pos() >= (300,100):
        print("Bug win")
        break
    elif elseif.pos() >= (300,-100):
        print("Elseif win")
        break
sleep(30)
