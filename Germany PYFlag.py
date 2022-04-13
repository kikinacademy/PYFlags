import turtle
t = turtle.Turtle()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(100)
  t.left(90)

t.color('yellow')
t.begin_fill()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(33)
  t.left(90)
t.end_fill()

t.left(90)
t.forward(33)
t.left(270)

t.color('red')
t.begin_fill()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(33)
  t.left(90)

t.end_fill()
t.left(90)
t.forward(33)
t.left(270)

t.color('black')
t.begin_fill()

for i in range(2):
  t.forward(200)
  t.left(90)
  t.forward(33)
  t.left(90)

t.end_fill()

