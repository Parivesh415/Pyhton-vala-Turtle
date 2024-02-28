import turtle as t

# Set up the screen
screen = t.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Chhota Bheem's head
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.color("green")
t.circle(50)
t.end_fill()

# Chhota Bheem's body
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.color("green")
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.end_fill()

# Chhota Bheem's eyes
t.penup()
t.goto(-20, 10)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(15)
t.end_fill()

t.penup()
t.goto(20, 10)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(15)
t.end_fill()

# Chhota Bheem's pupils
t.penup()
t.goto(-15, 20)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(7)
t.end_fill()

t.penup()
t.goto(25, 20)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(7)
t.end_fill()

# Chhota Bheem's mouth
t.penup()
t.goto(0, -15)
t.pendown()
t.setheading(90)
t.circle(20, 180)

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()
