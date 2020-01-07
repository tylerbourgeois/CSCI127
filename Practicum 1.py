import turtle

def bobcat_line(turtle, segments, length):
    for i in range(segments):
        if ((i % 2) == 0):
            turtle.color("blue")
        else:
            turtle.color("gold")
        turtle.forward(length)
        
drawing_turtle = turtle.Turtle()
drawing_turtle.width(3)
drawing_turtle.hideturtle

number_segments = int(input("Enter number of Segments: " ))
segment_length = int(input("Enter length of a segment: " ))
bobcat_line(drawing_turtle, number_segments, segment_length)
