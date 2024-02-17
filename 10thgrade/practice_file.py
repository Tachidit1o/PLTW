import turtle as trtl 
painter = trtl.Turtle()
painter.shape('turtle')

x = 0
y = 0 
height = 63
painter.pencolor ('blue')

for count in range(height):
    painter.goto(x,y)
    painter.fd(50)
    y = y + 1
    remainder = count % 12

    if (count > 42):
        x = 200
        y = 0
      
        if (remainder > 6 ):
            painter.pencolor('red')

        else: 
            painter.pencolor('blue')
    elif(count > 21):
        x = 100 
        if (remainder > 6 ):
            painter.pencolor('red')
        else: 
            painter.pencolor('blue')
    elif (count<21): 
        if (remainder > 6 ):
            painter.pencolor('red')
        else: 
            painter.pencolor('blue')
    
        

    

wn =trtl.Screen()
wn.mainloop()
