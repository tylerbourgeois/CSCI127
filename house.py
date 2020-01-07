import turtle

square = turtle.Turtle()
square.hideturtle()

rectangle = turtle.Turtle()
rectangle.hideturtle()

triangle = turtle.Turtle()
triangle.hideturtle()

def drawsquare(x, y, side):
    square.up()
    square.goto(x,y)
    square.down()
    for i in range(4):
        square.forward(side)
        square.right(90)

drawsquare(-50, 50, 100)
drawsquare(-30, 30, 20)
drawsquare(10, 30, 20)

triangle.up()
triangle.color("red")
triangle.goto(-50, 50)
triangle.down()
triangle.begin_fill()
triangle.goto(0, 100)
triangle.goto(50, 50)
triangle.goto(-50, 50)
triangle.end_fill()

rectangle.up()
rectangle.goto(-10, -10)
rectangle.down()
rectangle.begin_fill()
for half in range(2):
    rectangle.forward(20)
    rectangle.right(90)
    rectangle.forward(40)
    rectangle.right(90)
rectangle.end_fill()

