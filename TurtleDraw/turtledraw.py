from turtle import Turtle
from turtle import Screen
import random
  
# Defining method to draw a full heart
def heart(pen, size):
    #get random angle oreintation
    ANGLE = random.randint(-45, 45)
    LEFT = 140 + ANGLE
    FORWARD = 180 * size
    CIRCLE = -90 * size
    HEADING = 60 + ANGLE

    #define width and height to draw hearts
    screenWidth = 300
    screenHeight = 300

    #go to random spot on screen
    x = random.randint(-screenWidth, screenWidth - 1)
    y = random.randint(-screenHeight, screenHeight -1)
    
    pen.penup()
    pen.goto(x,y)
    pen.setheading(0)

    #get random fill color
    pick = random.randint(1,3)
    if pick == 1:
        pen.color('black')
        pen.fillcolor('red')
    elif pick == 2:
        pen.color('black')
        pen.fillcolor('pink')
    elif pick == 3:
        pen.color('black')
        pen.fillcolor('white')
        

    pen.begin_fill()
    pen.down()
    
    #curve one
    pen.left(LEFT)
    pen.forward(FORWARD)
    pen.circle(CIRCLE, 200)
    pen.setheading(HEADING)

    #second curve
    pen.circle(CIRCLE, 200)
    pen.forward(FORWARD)

    pen.end_fill()
    pen.up()

#recursivly draw hearts
def recursiveHearts(pen,size,delta):
    heart(pen,size)
    if size > .1:
        recursiveHearts(pen,size * delta, delta)
        
    

#set up the main
def main():
    t = Turtle()
    s = Screen()
    s.bgcolor("black")
    t.setpos(0,0)
    t.speed(1)
    
    recursiveHearts(t, 1, .9)
    t.hideturtle()

main()
