import turtle

turtle.Screen().bgcolor("Sky blue")
board = turtle.Turtle()
board.width(5)
board.pencolor("purple")
board.speed(6)

#first triangle for star
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()