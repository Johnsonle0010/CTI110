## Leon Johnson

## 04/06/2024

## P4LAB1b


import turtle

# Set up the turtle screen
screen = turtle.Screen()
##Name Tutle Screen
screen.title("Initials: LJ")
## # Changes Backbround color to Black
screen.bgcolor("Black")  

# Create a turtle for drawing
pen = turtle.Turtle()


# Draw the letter 'L'
# Position for 'L'
pen.penup()
pen.goto(-100, 100)  # Centering in the screen
pen.pendown()
pen.pensize(10)
pen.pencolor("Blue")
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(100)

# Draw the letter 'J'
pen.penup()
pen.goto(200, 20) # Position for Letter J in the screen
pen.pendown()
pen.pensize(10)
pen.pencolor("Red")
pen.goto(200, -50)  # postion to add the curve for letter J
pen.right(90)
pen.circle(-90, 180)
pen.pendown()




