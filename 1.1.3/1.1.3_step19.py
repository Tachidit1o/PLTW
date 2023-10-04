import turtle as trtl

painter = trtl.Turtle()

x = -150
y = -200

floors = 63

painter.penup()
painter.goto(x,y)
painter.pendown()
painter.forward(50)

for me in range(floors):



    remainder = me % 63
    if remainder >= 42:
        painter.pencolor("green")
    elif remainder >= 21: 
        painter.pencolor("red")

    y += 5


wn = trtl.Screen()
wn.mainloop()

Hello