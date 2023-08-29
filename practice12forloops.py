import turtle as trtl
painter = trtl.Turtle()

painter.penup()
painter.goto(-10, -100)
painter.pendown()

for move in range(8):
    painter.forward(50)
    painter.right(45)

painter.penup()
painter.goto(120,100)
painter.pendown()

for move in range(8):
    painter.forward(50)
    painter.left(45)

painter.penup()
painter.goto(-170, 220)
painter.pendown()

for move in range(8):
    painter.forward(50)
    painter.right(45)

wn = trtl.Screen()
wn.mainloop()