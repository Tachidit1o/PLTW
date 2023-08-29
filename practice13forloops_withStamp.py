import turtle as trtl 
painter = trtl.Turtle()
painter.color("blue")
painter.shape("circle")
painter.fillcolor("red")

for move in range(5):
    painter.circle(20)
    painter.penup()
    painter.forward(50)
    painter.right(75)
    painter.pendown()
    

wn = trtl.Screen()
wn.mainloop()