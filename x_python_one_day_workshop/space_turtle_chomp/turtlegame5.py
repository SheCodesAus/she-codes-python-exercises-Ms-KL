# Turtle Graphics Game - Space Turtle Chomp

import turtle
    # for turtle elements, funcs and objects
import math
    # for collision checking
import random
    # for cabbage randomness

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

# ------- Set Goal: Create food
food = turtle.Turtle()
    # creates food variable with a Turtle object from turtle module
food.color("lightgreen")
    # sets food to green
food.shape("circle")
    # sets food shape to circle
food.penup()
    # prevents food from drawing
food.speed(0)
    # makes food appear immediately
food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    # creates food in a random position between the boundaries set by random integer values = same as the boundaries for where the turtle bounces

    # ALT: (-100, 100)
    # x -100 move 100 points from 0 center to the left (neg) side
    # y 100 move 100 points from 0 center to the top (pos) line
    # 0 = center
    # y -100 = move towards bottom line from center 0
    # y 100 = move towards top line from center 0
    # x -100 = move towards left line from center 0
    # x 100 = move towards right line from center 0

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

def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
    # replaces the general collision function with a user function to use in other codeblocks
    # uses general t1 instead of turtle or food to be used elsewhere
    # t1 xcord - t2 xcord, then square the result
    # do the same for t1 ycord and t2 ycord
    # add the results together
    # find square root of result = d
    # if the d < 20 (within 20 points of eachother) then = true
    # otherwise = false
    # use true/false to dictate next move

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
    
    # ------- collision detection
        # import math and use pythagoras to work out where turtle and cabbage are, if they are touching or if distance is small between them
        # original format using ALT. simplified by replacing with isCollision to reuse code
    if isCollision(player,food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    # if the result of calling def function isCollision with t1 as player and t2 as food = TRUE, then set the position of food at the random x and y within the set boundaries
    # ALT:
    # d = math.sqrt(math.pow(player.xcor() - food.xcor(), 2) + math.pow(player.ycor() - food.ycor(),2))
        # xcor cabbage - xcor player
        # sqr it (result x result)
        # repeat for ycor
        # add results together
        # find sqr root of results = d
    # if d < 20:
        # food.setposition(random.randint(-290, 290), random.randint(-290, 290))
        # when collision happens, move the food to a random position between the boundaries set by random integer values = same as the boundaries for where the turtle bounces
        
        # ALT: food.hideturtle()
        # if the result is less than 20 (turtle and cabbage close to eachother), hide the cabbage

