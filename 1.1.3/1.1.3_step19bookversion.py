import turtle as trtl

painter = trtl.Turtle()

x = -100
y = -100

num_of_floors = 63

for lines in range(num_of_floors):
    painter.penup()
    painter.goto(x,y)
    painter.pendown()
    painter.forward(10)

    remainder = lines % 63
    if remainder >= 56:
        painter.pencolor("green")
    elif remainder >= 49:
        painter.pencolor("red")
    elif remainder >= 42: 
        x = 0

        painter.pencolor ("pink")
    elif remainder >= 35: 
        painter.pencolor ("black")
    elif remainder >= 28: 
        painter.pencolor("yellow")
    elif remainder >= 21: 
        x = -50
        painter.pencolor("grey")
    elif remainder >= 14: 
        painter.pencolor("blue")
    elif remainder >= 7:
        painter.pencolor("lime green")

    new_remainder = lines % 21
    if new_remainder == 0:
        y = -100

    y = y + 5 

wn = trtl.Screen()

wn.mainloop()