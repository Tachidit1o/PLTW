import turtle as trtl 

#Setting up window first because otherwise 
#default window opens up and then our window code widens it...
wn = trtl.Screen()
wn.setup(width = 1000, height = 1000)

#Fist you create an object
painter = trtl.Turtle()
painter.penup()

angle = 90
radius = 90
length = 100
color = 'green'
answer = input('Press y to begin? ')
while answer == 'y':
    painter.pendown()
    painter.fillcolor(color)
    painter.rt(angle)
    painter.fd(length)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()
    answer = input('Press n to stop, otherwise press y to continue.')




wn.mainloop()