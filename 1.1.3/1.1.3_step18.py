import turtle as trtl 

painter = trtl.Turtle()

painter.pensize(2)
painter.pencolor("grey")

x = -100
y = -150

num_of_floors = 63

for little_guy in range(num_of_floors):
    painter.penup()
    painter.goto(x,y)
    painter.pendown()
    painter.forward(50)
    
    axe = little_guy % 63
    if axe >= 42  : 
        painter.pencolor("red")
    elif axe >=  21:
        painter.pencolor("blue")

    y += 5


wn = trtl.Screen()
wn.mainloop()