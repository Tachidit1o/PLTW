import turtle as trtl 
painter = trtl.Turtle()
painter.shape('turtle')

x = 0
y = 0 
height = 63
painter.pencolor ('blue')
painter.penup()

for count in range(height):
    painter.goto(x,y)
    painter.pendown()
    painter.fd(50)
    y = y + 1
    remainder = count % 12

    if (remainder > 6 ):
        painter.pencolor('blue')
    else: 
        painter.pencolor('red')
    {'''
    Code to add three colors: 

    if (remainder > 8 ):
        painter.pencolor('blue')
    elif (remainder >4): 
        painter.pencolor('red')
    else: 
        painter.pencolor('green')
    '''}
    if count == 36:
        painter.penup()
        x = x + 100
        y = 0
    elif count == 19:
        painter.penup()
        x = 100
        y = 0

wn =trtl.Screen()
wn.mainloop()
