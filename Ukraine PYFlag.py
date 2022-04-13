import turtle, time
t = turtle.Turtle()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(100)
  t.left(90)

t.color('royalblue')
t.begin_fill()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(50)
  t.left(90)
t.end_fill()

t.left(90)
t.forward(50)
t.left(270)

t.color('gold')
t.begin_fill()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(50)
  t.left(90)

t.end_fill()
t.left(90)
t.forward(33)
t.left(270)

t.end_fill()


style = ('Courier', 30, 'italic')
t.color('black')
turtle.penup()
turtle.goto(-220, -100)
turtle.pendown()
turtle.write('SAY YES TO PEACE!🕊️🏳️', font=style, align='left')

time.sleep(2)
