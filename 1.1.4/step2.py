#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors
color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
height = 50 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle = 65 # experiment with the shape
seg = int(360/angle)

while (painter.ycor() < height):
  if (space % 2 == 0):
    painter.fillcolor(color1)
    painter.color(color1)
  elif (space % 5 == 0):
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(120)
  painter.forward(7*space + 10) # experiment
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1

wn.mainloop()