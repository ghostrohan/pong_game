
import turtle


wn = turtle.Screen()
wn.title("Pong Game")
wn.setup(width=800, height=600)
wn.bgpic("back.gif")
wn.tracer(0)

# Score 

score_A = 0;
score_B = 0;

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=12 ,stretch_len= 1) 
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-375,0)

# paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=12, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(375, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("brown")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Score System

pen = turtle.Turtle()
pen.speed(0)
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A : {} Player B : {}".format(score_A,score_B),align="center",font = ("Courier", 24,"normal"))




flag = True
log = []
# Initilalizing log
log.append(0.1)

# To Avoid the game being boring when ever a game restarts
# the spped is set to a differnt value
# Ideally the median in the min - max can be used
# As if the player is losing at the lower levels quickly
# It will return the most ideal speed at which the game can be played
# And vice versa
# We can use a list to do this

def update_speed(log): 
    n = len(log) - 1
    mini = log[0]
    maxi = log[n]
    return min(3, (mini + maxi)/2)  # seting an upper limit


# Function to move paddle A

def paddle_A_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_A_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

# Function to move paddle B

def paddle_B_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_B_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#exit functionality

def exit_game():
    global flag
    flag = False

# Keyboard Binding

wn.listen()
wn.onkeypress(paddle_A_up,"w")
wn.onkeypress(paddle_A_down,"s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")
wn.onkeypress(exit_game, "e")

while flag:
    wn.update()
    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball out of bounds change in Y Direction
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy*-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy*-1
    # Ball out of bounds change in X Direction
    if ball.xcor() > 360:
        print(ball.dx)
        log.append(abs(ball.dx))
        ball.goto(0,0)
        ball.dx = update_speed(log)
        ball.dx *= -1
        paddle_a.sety(0)
        paddle_b.sety(0)
        score_A += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -360:
        print(ball.dx)
        log.append(abs(ball.dx))
        ball.goto(0, 0)
        ball.dx = update_speed(log)
        ball.dx *= 1
        paddle_a.sety(0)
        paddle_b.sety(0)
        score_B += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_A,score_B),align="center",font = ("Courier", 24,"normal"));
    
    # Ball Bounce out of Paddle 
    if  ball.xcor() > 340  and ball.ycor()  > paddle_b.ycor() - 100 and ball.ycor()  < paddle_b.ycor() + 100:
        if(ball.dx < 3 or ball.dx > -3):
            if(ball.dx > 0):
                ball.dx += 0.01
            else:
                ball.dx -= 0.01
        ball.dx *= -1
    elif ball.xcor() < -340 and ball.ycor()  > paddle_a.ycor() - 100  and ball.ycor()  < paddle_a.ycor() + 100:
        if(ball.dx < 3 or ball.dx > -3):
            if(ball.dx > 0):
                ball.dx += 0.01
            else:
                ball.dx -= 0.01
        ball.dx *= -1
