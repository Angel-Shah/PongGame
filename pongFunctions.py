''' file created with a copy of all the functions used in the pong game as when calling the pong
 script as a module in test_pong, the file kept running the game instead of the test'''

import turtle

paddle1 = turtle.Turtle()


paddle2 = turtle.Turtle()


def paddle1_up(x):
    y = paddle1.ycor()
    y += 25
    paddle1.sety(y)
    return x + 25


def paddle1_down(x):
    y = paddle1.ycor()
    y -= 25
    paddle1.sety(y)
    return x - 25


def paddle2_up(x):
    y = paddle2.ycor()
    y += 25
    paddle2.sety(y)
    return x + 25


def paddle2_down(x):
    y = paddle2.ycor()
    y -= 25
    paddle2.sety(y)
    return x - 25


turtle.done()