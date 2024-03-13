import turtle as trtl

wn = trtl.Screen()
wn.setup(width = 1300, height = 800)

painter= trtl.Turtle()
painter.shape("turtle")
painter.penup()

line = 2
while (line % 2 !=2):
    painter.goto(-400,-300)
    painter.pendown()
    painter.circle(50)
    painter.penup()
    painter.goto(400, 300)
    painter.pendown()
    painter.circle(50)
    painter.penup()
    painter.goto(-400, 300)
    painter.pendown()
    painter.circle(50)
    painter.penup()
    painter.goto(400, -300)
    painter.pendown()
    painter.circle(50)
    painter.penup()
    line += 1
    if line % 6 == 0: 
        painter.color('salmon')
    elif line % 3 == 0: 
        painter.color('green')
    else:
        painter.color('yellow')

wn.mainloop()