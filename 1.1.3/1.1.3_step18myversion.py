import turtle as trtl 

painter = trtl.Turtle()

painter.pensize(2)
painter.pencolor("grey")

x = -100
y = -150

num_of_floors = 63

for little_guy in range(num_of_floors):
    painter.penup()

    axe = little_guy % 63
    if axe > 42: 
        painter.pencolor("red")
        x = 100
    
    elif axe >  21:
        painter.penup()
        painter.pencolor("blue")
        x = 0
# Note: Students might get stuck with the following:
    if little_guy % 21 == 0:     
        y = -150

    painter.goto(x, y)
    painter.pendown()
    painter.forward(50)

    y = y + 5




wn = trtl.Screen()
wn.mainloop()