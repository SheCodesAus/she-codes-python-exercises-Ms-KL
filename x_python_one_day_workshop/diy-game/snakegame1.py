# Kristy's exercise: snake using turtle module

# Turtle Graphics Game - Space Turtle Chomp

import turtle
snake=turtle
#rename turtle to snake

# ------- setup screen

snake.setup (650,650)
    #sets up the size of the screen in the window
gamecanvas = snake.Screen()
    # wn = name of screen --> .Screen ()
gamecanvas.bgcolor('black')
    # sets the color of the screen

# ------- create player snake
player = snake.Turtle()
    # calls on the snake module and creates a .Turtle object
    # renames Turtle to snake
player.color('white')
    # dictates that player is orange
player.shape('square')
    # dictates that player is shaped like a square
player.penup()
    # dictates that the turtle should stop drawing when moving
player.shapesize(1,3,1)
    # height, width, radius
        # 10,1,1
            # 10 high, 1 wide, no radius
        # 1,10,1
            # 1 high, 10 wide, no radius
        # 1,1,10
            # 1 high, 1 wide, 10 radius (Curved edges/no corners)

# ------- set speed variable
speed = 1
    # player snake will move across screen at speed of 1

# ------- make snake move
while True:
    player.forward(speed)
    #which this loop is true (forever), move player forward at the speed set in above variable



