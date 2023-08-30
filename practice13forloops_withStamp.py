import turtle as trtl 
painter = trtl.Turtle()

painter.penup()
painter.goto(-50,160)
painter.pendown()
painter.shape("circle")
painter.fillcolor("blue")


for move in range(7):
    painter.stamp()
    painter.penup()
    painter.forward(140)
    painter.right(45)
    painter.pendown()

    newnum = move % 2
    if newnum == 0:
        painter.fillcolor("red")
    else: 
        painter.fillcolor("blue")
    

wn = trtl.Screen()
wn.mainloop()