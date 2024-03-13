import turtle as trtl

wn = trtl.Screen()
wn.setup(width = 800, height = 600)

painter = trtl.Turtle()
painter.shape("turtle")

length = 100
angle = 45
diameter = 100
color = "blue"

question = input('Type y to loop: ')
while (question == 'y'):
    painter.rt(angle)
    painter.fd(length)
    painter.begin_fill()
    painter.circle(diameter)
    painter.end_fill()
    question = input('Type y to loop: ')

wn.mainloop()