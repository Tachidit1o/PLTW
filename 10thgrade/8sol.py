#   a113_circle_of_circles.py
#   Modify this code to draw a circle of circles
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")


for x in range(18):
  painter.shape("circle")
  painter.stamp()
  painter.forward(20)
  painter.right(20)

wn = trtl.Screen()
wn.mainloop()