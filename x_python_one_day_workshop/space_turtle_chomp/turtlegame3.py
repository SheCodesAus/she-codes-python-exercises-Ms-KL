# Turtle Graphics Game - Space Turtle Chomp

import turtle

# ------- setup screen
turtle.setup (650,650)
    #sets up the size of the screen in the window
wn = turtle.Screen()
    # wn = name of screen --> .Screen ()
wn.bgcolor('navy')
    # sets the color of the screen

# ------- draw border
mypen = turtle.Turtle()
    # variable set mypen
    # calls on turtle module
    # creates a player called mypen using .Turtle() object
mypen.penup()
    # default turtle object has pen down. bring up so it doesn't draw
mypen.setposition(-300,-300)
    # places the turtle mypen to a specific spot - top left
mypen.pendown()
    # returns the pen back down
mypen.pensize(3)
    # sets the thickness of the pen to draw
mypen.color('white')
    # set the pen stroke to white
mypen.speed(0)
    # sets the speed of mypen to max - so you don't see the box being drawn
    # comment out if you want to see the box being drawn
for side in range(4):
    # for elm in range of 4... for each 1 within the 4
    # for each SIDE in the 4 sides
    mypen.forward(600)
        #move the pen forward 600p points (draw)
        # THEN
    mypen.left(90)
        # move the pen left 90 degrees
    # repeat steps 4 times (creates a square)
mypen.hideturtle()
    # makes turtle invisible to speed up drawing


# ------- create player turtle
player = turtle.Turtle()
    # calls on the turtle module and creates a .Turtle object named player
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

    # ------- boundary setting for turtle
        # set in the while loop as it needs to happen while the turtle is moving
        # 290 / -290 are the boundaries of the drawn border in mypen, hence below
    
    if player.xcor() > 290 or player.xcor() < -290:
        # if the player's x coord (LEFT OR RIGHT) is more than 290 (R) or less than -290 (L)
        player.right(180)
        # bounce off at 180 degrees
    
    if player.ycor() > 290 or player.ycor() < -290:
        # if the player's y coord (TOP or BOTTOM) is more than 290 (T) or less than -290 (B)
        player.right(180)
        # bounce off at 180 degrees

