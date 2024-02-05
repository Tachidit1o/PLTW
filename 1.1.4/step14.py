##############################################################################
#   a114_TR_nested_loops_3.py
#   Example solution
##############################################################################
import turtle as trtl

color1 = "red" # changed colors
color2 = "blue"

wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  painter.color(color1)
  space = 1

  angle = int(input("angle:"))
  
  while painter.ycor() < height: 
    if space % 200 == 0: # updated
      painter.fillcolor(color1) 
      painter.color(color1) 
      print (space)
    elif space % 100 == 0:#updated
      painter.fillcolor(color2) 
      painter.color(color2) 
      print (space)
      
    painter.right(angle) 
    painter.forward(2 * space + 10) # experiment 
    painter.begin_fill() 
    painter.circle(3) 
    painter.end_fill() 
    space = space + 1

  answer = input("again?")

wn.bye()
