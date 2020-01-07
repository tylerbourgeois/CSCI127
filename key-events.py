
import turtle

window = turtle.Screen()

drawer = turtle.Turtle()
drawer.speed(0)

def east():
    drawer.setheading(0)
    drawer.forward(50)

def north():
    drawer.setheading(90)
    drawer.forward(50)

def west():
    drawer.setheading(180)
    drawer.forward(50)

def south():
    drawer.setheading(270)
    drawer.forward(50)

def forward():
    drawer.forward(50)

def turn():
    drawer.right(45)

window.onkey(east, "Right")
window.onkey(north, "Up")
window.onkey(west, "Left")
window.onkey(south, "Down")
window.onkey(forward, "f")
window.onkey(forward, "F")
window.onkey(turn, "r")
window.onkey(turn, "R")
window.onkey(turn, "PageDown")

window.listen()

window.exitonclick()
