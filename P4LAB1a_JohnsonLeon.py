## Leon Johnson

## 04/06/2024

## P4LAB1a


##Import Turtle Sets the drawing board 
import turtle
# Set up the window and its attributes
wn = turtle.Screen()         
wn.bgcolor("lightblue")
wn.title("Drawing Shapes with Turles")

## Changes the triangle shape to a Turtle
turtle.shape('turtle')

## Naming the Turtle Bob and Dani
Dani = turtle.Turtle()
Bob = turtle.Turtle()

# Move forward by 100 units
for _ in range(4):
    Bob.forward(100)
# Turn right by 90 degrees 4 times
    Bob.right(90)

##Moves Dani to a new position so shapes do not overlap
Dani.penup()
Dani.goto(100, -50)  
Dani.pendown()

# Move forward by 100 units
for _ in range(3):
    Dani.forward(100)
    
# Turn right by 120 degrees 3 times   
    Dani.left(120)
