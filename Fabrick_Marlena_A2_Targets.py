# PROGRAMMER:    Marlena Fabrick
# PROGRAM NAME: Turtle Graphics — Target Design
# DATE WRITTEN: September 20, 2020
# PURPOSE:      This program will demonstrate how to create a basic graphical design

import turtle # finding the module turtle and making it available inside python


def draw_circle(x, y, radius, fill_color):
    """Draws a filled circle at the given screen position."""
    turtle.fillcolor(fill_color)  # define color to fill shape
    turtle.begin_fill()           # begin filling in shape
    turtle.penup()
    turtle.goto(x, y)             # Moves turtle to absolute screen position
    turtle.pendown()
    turtle.circle(radius)         # Draw a circle with the given radius
    turtle.end_fill()             # End filling in shape


# Change background color
turtle.bgcolor("pink")
turtle.speed(10)        # slows down speed of drawing
turtle.shape("turtle")  # arrow, circle, diamond, turtle
turtle.width(5)         # width of the line / pen
turtle.pencolor("purple")

# Make a graphical design

# Add first circle — radius 100 (white)
draw_circle(0, -36, 100, "white")

# Add second circle — radius 50 (turquoise)
draw_circle(0, -18, 50, "turquoise")

# Add third circle — radius 25 (white)
draw_circle(0, -9, 25, "white")

# Hide the turtle cursor and keep the window open
turtle.hideturtle()
turtle.done()
