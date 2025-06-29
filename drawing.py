''''
import turtle
#creating canvas
turtle.Screen().bgcolor("Orange")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to Turtle Window")

#turtle object creation
board = turtle.Turtle()
board.speed(2)

#creating a saquare 
for i in range(4):
    board.forward(100)
    board.left(90)
    i =i + 1
'''
import turtle
#creating canvas
turtle.Screen().bgcolor("Orange")
board = turtle.Turtle()
#first triangle for star
board.forward(100)# draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()
