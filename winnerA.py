import turtle


window = turtle.Screen()
window.title("Winner")
window.setup(width=1200, height=600)
window.bgcolor("black")
# this helps game run faster
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.hideturtle()
pen.penup()
pen.goto(0, 0)
pen.write("<== Player A WINS!", align = "center", font =("Courier", 40, "bold"))
pen.penup()


turtle.done()
