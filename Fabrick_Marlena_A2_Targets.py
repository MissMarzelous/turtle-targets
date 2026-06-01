# PROGRAMMER:    Marlena Fabrick
# PROGRAM NAME: Sample 1 Square Graphical Design
# DATE WRITTEN: September 20, 2020

# This program will demonstrate how to crete basic graphical design

import turtle; # finding the module turtle and making it availabe inside python
 
# Change background color
turtle.bgcolor("pink")

turtle.speed(10) # slows down speed of drawing
turtle.shape("turtle") # arrow, circle, diamond, turtle
turtle.width(5) # width of the line / pen
turtle.pencolor("purple")

# Make a graphical design

# Add first circle.


turtle.fillcolor("white")  # define color to fill shape
turtle.begin_fill()       # begin filling in shape
turtle.penup()
turtle.goto(0, -36) # Moves turtle to absolute screen position
turtle.pendown()
turtle.circle(100) # Draw a circle with a radius of 100
turtle.end_fill()  # End filling in shape

turtle.fillcolor("turquoise") # define color to fill shape
turtle.begin_fill() # begin filling in shape
turtle.penup()
turtle.goto(0, -18)# Moves turtle to absolute screen position
turtle.pendown()
turtle.circle(50) # Draw a circle with a radius of 50
turtle.end_fill() # End filling in shape

turtle.fillcolor("white")  # define color to fill shape
turtle.begin_fill() # begin filling in shape
turtle.penup()
turtle.goto(0, -9)# Moves turtle to absolute screen position
turtle.pendown()

turtle.circle(25) # Draw a circle with a radius of 25
turtle.end_fill() # End filling in shape
