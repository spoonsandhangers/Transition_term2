# This is a challenge using loops and the
# python turtle graphics library/module
#

# starter

# word = "W"
# my_word = "inner"
#
# for i in range(len(my_word)):
#     word = word + my_word[i]
#
# print(word)

# turtle is a graphics library you can import
# it draws lines and shapes using a turtle
# you can change the turtle to another shape or get rid of it all together.

# import turtle
#
# wn = turtle.Screen()
# bob = turtle.Turtle()
# bob.shape("turtle")
# bob.pencolor("red")
# bob.pensize(10)
# bob.speed(5)
#
# bob.forward(100)
# bob.right(45)
# bob.backward(150)
# bob.right(90)
# bob.forward(150)
# bob.left(135)
# bob.forward(100)
#
# wn.exitonclick()

# what does this draw
# it's a really long winded way to draw a triangle
# play around with some instructions and see what you can draw 5 mins
# change the pen colour, size and speed of the turtle
# you've got 5 mins to experiment

# wn = turtle.Screen()    # creates a graphics window to draw in
# jim = turtle.Turtle()   # creates a turtle called jim
# jim.forward(50)         # moves jim forward 50
# jim.right(90)           # turns jim 90 degrees
# jim.forward(50)         # moves jim forward 50
# wn.exitonclick()

# can you finish this code so that the turtle jim draws a square

# Can you modify this code to use a loop to draw the square

# wn = turtle.Screen()
# jim = turtle.Turtle()
#
# for i in range(4):
# 	jim.forward(50)
# 	jim.right(90)
#
# wn.exitonclick()

# Make this a subroutine using def called square, so that anytime you want to draw a square
# you can just type square()
# extension - the size of the square should be determined by a parameter
# passed to the subroutine
# ask a user to select the size of the square and then draw a square for them
# import turtle
# extension 2 - use a fill colour to fill the shape.
#
# wn = turtle.Screen()
# jim = turtle.Turtle()
#
#
# def square(size):
# 	jim.fillcolor("red")
# 	jim.begin_fill()
# 	for i in range(4):
# 		jim.forward(size)
# 		jim.right(90)
# 	jim.end_fill()
#
# square(100)
# square(50)
#
# wn.exitonclick()


# this is how you fill in a shape:

# import turtle
#
# wn = turtle.Screen()
# jim = turtle.Turtle()
#
# jim.fillcolor("red")
# # begin to fill before you draw the shape
# jim.begin_fill()
#
# for i in range(3):
# 	jim.forward(100)
# 	jim.right(120)
#
# # end fill when you have completed drawing the shape.
# jim.end_fill()
#
# wn.exitonclick()

# if you want to move your turtle without leaving a trail
# you can use penup() and pendown()
# to send a turtle to a particular place you can use goto(x,y)


# import turtle
#
# wn = turtle.Screen()
# jim = turtle.Turtle()
# jim.speed(10)
# jim.pencolor("blue")
#
# jim.backward(100)
# jim.right(90)
# jim.forward(100)
# jim.left(90)
# jim.forward(100)
# jim.right(90)
# jim.forward(100)
# jim.right(90)
# jim.forward(100)
#
# # after I draw the first letter I lift up the pen
# # and get into position to draw the second.
# jim.penup()
# jim.backward(200)
# # then I put the pen down
# jim.pendown()
#
# jim.backward(100)
# jim.right(90)
# jim.forward(200)
# jim.left(90)
# jim.forward(100)
# jim.backward(200)
#
# wn.exitonclick()

# can you draw out your initials using turtle.
# make sure they are not joined together by using pen up.

###############################################
# drawing shapes with for loops and turtle
# When drawing a square the ange for the four loop was 4
# as there are 4 sides and 4 angles
# Each angle in a square is 90 degrees
# To work out what angle to use we need to divide the degrees in a full turn
# by the number of sides in th shape.
# e.g. a square has 4 sides.
# A full turn is 360 degrees
# So we work ou the angle = 360/4 = 90 degrees

# Can you draw the following shapes using for loops:
# a triangle - 3 sides
# a pentagon - 5 sides
# a hexagon - 6 sides
# an octagon - 8 sides

# extension - make a subroutine that accepts an integer as a parameter that
# is the number of sides the shape should have, then draws the shape
# extension - pass 2 more parameters into the subroutine that specify
# where you want the shape to be drawn on the screen
# extension - add another parameter that passes in the turtle that should be used to draw the shape.

# import turtle
#
# wn = turtle.Screen()
# bob = turtle.Turtle()
#
# def drawShape(sides,x,y,turt):
# 	angle = 360/sides
# 	turt.penup()
# 	turt.goto(x,y)
# 	turt.pendown()
# 	for count in range(sides):
# 		turt.fd(100)
# 		turt.right(angle)
#
# drawShape(3,100,100,bob)
# drawShape(6,-100,0,bob)
#
# wn.exitonclick()

# Homework
# What is the output of this code
# import turtle
#
# wn = turtle.Screen()
# bob = turtle.Turtle()
# bob.speed(11)
# bob.penup()
# bob.goto(-300,0)
# bob.pendown()
#
# for count in range(20):
# 	bob.penup()
# 	bob.fd(10)
# 	bob.pendown()
# 	bob.fd(20)
#
# wn.exitonclick()
