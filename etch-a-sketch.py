import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

square.up()
square.goto(-200, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-205, 205)
square.write("Change Color")
square.goto(-200, 200)

pencil = turtle.Turtle()
pencil.shape("circle")

square.goto(-200, 200)
square.down()

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        color_1 = random.random()
        color_2 = random.random()
        color_3 = random.random()
        pencil.color(color_1, color_2, color_3)
        square.color(color_1, color_2, color_3)
        for i in range(4):
            square.forward(50)
            square.right(90)


        
window.onclick(drawing_controls)

pencil.onrelease(pencil.goto)

