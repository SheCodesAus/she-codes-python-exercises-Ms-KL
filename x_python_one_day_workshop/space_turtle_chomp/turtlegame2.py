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
player.speed(0)
    # stops turtle jumping
    # 0 = fastest animation speed

# ------- set speed variable
speed = 1
    # player turtle will move across screen at speed of 1

# ------- define functions to call in keyboard bindings
def turn_left():
    player.left(30)
    # turn the player left @30 degrees. Set this to function turn_left

def turn_right():
    player.right(30)
    # turn the player right @30 degrees. Set this to function turn_right

def increase_speed():
    global speed
    speed += 1
    # makes the speed function global to use inside any function
    # when called, increase the speed by 1

# ------- set keyboard binding
turtle.listen()
    # tells the computer to listen for commands to control game
turtle.onkey(turn_left, 'Left')
    # onkey = tells computer to use the turn the player 30 degrees using def turn_left when the left arrow is used
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
    # tells computer to increase speed by 1 when the up arrow is used

# ------- make turtle move
while True:
    player.forward(speed)
    #   while this loop is true (forever), move player forward at the (global) speed set in above variable.
