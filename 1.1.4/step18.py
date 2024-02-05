##############################################################################
#   a114_TR_nested_loop_4_and_opp.py
#      Use nested loops to draw two "peaks" plus the opposite of the original
##############################################################################
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1
while (x < 100):

  while (y < 100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1
  
  while (y > 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1

move_x = -1
move_y = -1
while (x > -100):

  while (y > -100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1
  
  while (y < 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1


wn = trtl.Screen()
wn.mainloop()