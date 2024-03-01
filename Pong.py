#Zuhayr Loonat
# PONG

# imports
import turtle
import time

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor(0,0,0)
sc.setup(width=1000, height=600)

# Create Paddels
def create_paddle(x, color):
    paddle = turtle.Turtle()
    paddle.speed(0)  # Set speed to 0 to disable animation
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()  # Don't draw a line while moving
    paddle.goto(x, 0)  # Set initial position
    return paddle

# Create left and right paddles
left_paddle = create_paddle(-400, "white")
right_paddle = create_paddle(400, "white")

# Ball Creation
ball = turtle.Turtle()
ball.speed(0)  # Set speed to 0 to disable animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # Set initial position
ball.dx = 4  # Ball's horizontal movement
ball.dy = 4  # Ball's vertical movement

# Movement
def move_left_paddleup():
    y = left_paddle.ycor()  # Get current y-coordinate
    y += 20  # Move up 20 pixels
    # Limit paddle movement within the screen
    if y > 220:
        y = 220
    left_paddle.sety(y)  # Update the y-coordinate

def move_right_paddleup():
    y = right_paddle.ycor()  # Get current y-coordinate
    y += 20  # Move up 20 pixels
    # Limit paddle movement within the screen
    if y > 220:
        y = 220
    right_paddle.sety(y)  # Update the y-coordinate

def move_left_paddledown():
    y = left_paddle.ycor()  # Get current y-coordinate
    y -= 20  # Move up 20 pixels
    # Limit paddle movement within the screen
    if y > 220:
        y = 220
    left_paddle.sety(y)  # Update the y-coordinate

def move_right_paddledown():
    y = right_paddle.ycor()  # Get current y-coordinate
    y -= 20  # Move up 20 pixels
    # Limit paddle movement within the screen
    if y > 220:
        y = 220
    right_paddle.sety(y)  # Update the y-coordinate

#Keybinds
# Bind key presses to the movement functions
sc.listen()
sc.onkeypress(move_left_paddleup, "w")  # "w" key moves left paddle up
sc.onkeypress(move_left_paddledown, "s")  # "s" key moves left paddle down
sc.onkeypress(move_right_paddleup, "Up")  # Up arrow key moves right paddle up
sc.onkeypress(move_right_paddledown, "Down")  # Down arrow key moves right paddle down


#GAMELOOP

while True:
    sc.update()  # Update the screen
    time.sleep(0.01)  # Delay for smoother animation

    # Update ball position
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for border collisions and bounce the ball
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1  # Reverse ball's vertical direction

    # Check for paddle collisions and bounce the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.dx *= -1  # Reverse ball's horizontal direction

# Close the window on exit
screen.exitonclick()