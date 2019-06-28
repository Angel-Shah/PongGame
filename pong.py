# importing the turtle module

import turtle
# import for sound effects on windows
import winsound

window = turtle.Screen()
window.title("Classic Pong Game")
window.setup(width=1200, height=600)
window.bgcolor("black")
# this helps game run faster
window.tracer(0)

# drawing dashed line down middle
line = turtle.Turtle()
line.speed(0)
line.width(2)
line.goto(0, 250)
line.color("white")
for i in range(13):
    line.setheading(270)
    line.forward(25)
    line.penup()
    line.forward(15)
    line.pendown()
    line.hideturtle()

# Drawing border
border = turtle.Turtle()
border.speed(0)
border.width(2)
border.color("white")
border.penup()
border.goto(-500, 250)
border.pendown()
border.forward(1000)
border.setheading(270)
border.forward(510)
border.setheading(180)
border.forward(1000)
border.setheading(90)
border.forward(510)
border.hideturtle()

# players scores
playerA = 0
playerB = 0

# Variable for finding winner
winner = 0

# pong ball


ball = turtle.Turtle()

# done for smoother animation
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid = 0.75, stretch_len = 0.75)
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


# player 1 paddle

paddle1 = turtle.Turtle()

# done for smoother animation
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.penup()
paddle1.goto(-460, 0)
paddle1.shapesize(stretch_wid=3, stretch_len=1)


# player 2 paddle

paddle2 = turtle.Turtle()

# done for smoother animation
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.penup()
paddle2.goto(460, 0)
paddle2.shapesize(stretch_wid=3, stretch_len=1)


# Scoreboard

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 250)
scoreboard.write("Player A: 0     Player B: 0", align = "center", font = ("Courier", 22, "bold"))

# pen for instructions

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-400, 250)
pen.write("'W' = up  'S' = down", align="center", font =("Courier", 12, "normal"))

pen.penup()
pen.goto(410, 250)
pen.write("'Up Arrow'= up  'Down Arrow'= down", align="center", font = ("Courier", 12, "normal"))

pen.penup()
pen.goto(0, -300)
pen.write(" First to 11 points WINS!", align="center", font = ("Courier", 16, "bold"))


# creating functions for moving paddles


def paddle1_up():
    y = paddle1.ycor()
    y += 25
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 25
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 25
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 25
    paddle2.sety(y)


# function for running winner files
def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())


# binding keyboard keys to move paddles

window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle1_up, "W")
window.onkeypress(paddle1_down, "S")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")


# loop for constantly updating window --------------------------------------------------------------------------------


while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # bouncing ball off ceiling and floor
    if ball.ycor() >= 242.5 or ball.ycor() <= -252.5:
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # increasing scores and resetting ball to middle after a player scores
    if ball.xcor() < -460:
        ball.goto(0, 0)

        playerB += 1
        scoreboard.clear()
        scoreboard.write("Player A: " + str(playerA) + "     Player B: " + str(playerB), align="center", font=("Courier", 22, "bold"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        ball.dx = -1
        ball.dy = 1

    if ball.xcor() > 460:
        ball.goto(0, 0)

        playerA += 1
        scoreboard.clear()
        scoreboard.write("Player A: " +str(playerA) + "     Player B: " + str(playerB), align="center", font=("Courier", 22, "bold"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        ball.dx = 1
        ball.dy = 1

    # bouncing ball off paddles
    if (ball.xcor() > 450 and ball.xcor() < 460) and (ball.ycor() < paddle2.ycor() + 30 and ball.ycor() > paddle2.ycor() - 30):
        ball.setx(450)
        ball.dx *= -1
        # changing bounce angles depending on where ball hits on paddle
        if (ball.ycor() > paddle2.ycor() + 5) and ball.dy < 0:
            ball.dy *= -1

        if (ball.ycor() < paddle2.ycor() - 5) and ball.dy > 0:
            ball.dy *= -1

        if ball.dx < 2 or ball.dy < 2:
            ball.dx *= 1.15
            ball.dy *= 1.15
        else:
            ball.dx = 2
            ball.dy = 2
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -450 and ball.xcor() > -460) and (ball.ycor() < paddle1.ycor() + 30 and ball.ycor() > paddle1.ycor() - 30 ):
        ball.setx(-450)
        ball.dx *= -1

        # changing bounce angles depending on where ball hits on paddle
        if (ball.ycor()> paddle1.ycor() + 5) and ball.dy < 0:
            ball.dy *= -1

        if (ball.ycor() < paddle1.ycor() - 5) and ball.dy > 0:
            ball.dy *= -1

        if ball.dx < 2 and ball.dy < 2:
            ball.dx *= 1.15
            ball.dy *= 1.15
        else:
            ball.dx = 2
            ball.dy = 2
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    # Checking if paddles are going off screen
    if paddle1.ycor() >= 220:
        paddle1.goto(-460, 220)
    if paddle1.ycor() <= -230:
        paddle1.goto(-460, -230)

    if paddle2.ycor() >= 220:
        paddle2.goto(460, 220)
    if paddle2.ycor() <= -230:
        paddle2.goto(460, -230)

    # checking for winner
    if playerA == 11:
        window.clear()
        run("winnerA.py")
        turtle.done()

    if playerB == 11:
        window.clear()
        run("winnerB.py")
        turtle.done()


