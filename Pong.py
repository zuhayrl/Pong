#Zuhayr Loonat
# PONG

# imports
import turtle

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
ball.dx = 2  # Ball's horizontal movement (change value for initial direction)
ball.dy = 2  # Ball's vertical movement
