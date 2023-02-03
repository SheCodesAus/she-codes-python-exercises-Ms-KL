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

# ------- create player snake
player = snake.Turtle()
    # calls on the snake module and creates a .Turtle object
    # renames Turtle to snake
player.color('white')
player.shape('square')
player.penup()
player.shapesize(1,3,1)
    # create initial snake
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

# -------  Define Functions
def move_left():
    player.left(90)

def move_right():
    player.right(90)

def move_up():
    player.up(90)

def move_down():
    player.down(90)


# -------  Set keyboard binding
snake.listen()
snake.onkey(move_left, 'Left')
snake.onkey(move_right, 'Right')
snake.onkey(move_up, 'Up')
snake.onkey(move_up, 'Down')
while True:
    player.forward(speed)


# ------- make snake move
while True:
    player.forward(speed)
    #which this loop is true (forever), move player forward at the speed set in above variable



