# Turtle Graphics Game - Space Turtle Chomp

import turtle

# ------- setup screen
turtle.setup (650,650)
    #sets up the size of the screen in the window
wn = turtle.Screen()
    # wn = name of screen --> .Screen ()
wn.bgcolor('navy')
    # sets the color of the screen

# ------- create player turtle
player = turtle.Turtle()
    # calls on the turtle module and creates a .Turtle named player
player.color('yellow')
    # dictates that player is orange
player.shape('turtle')
    # dictates that player is shaped like a turtle
player.penup()
    # dictates that the turtle should stop drawing when moving

# ------- set speed variable
speed = 1
    # player turtle will move across screen at speed of 1

# ------- make turtle move
while True:
    player.forward(speed)
    #which this loop is true (forever), move player forward at the speed set in above variable



