import turtle as trtl

painter = trtl.Turtle()

x = -150
y = -150

num_of_floors = 63

for runner in range(num_of_floors):

    painter.penup()

    remainder = runner % 6 
#teach the students that the remainder greater than or equal to 4 will be blue
    if remainder >= 4: 
        painter.pencolor("blue")

    elif remainder >= 2:
        painter.pencolor("red")
#Teach scholars that the below is how you start a new tower
    remainder = runner % 21
    if remainder == 0: 
        y = -150
        x = x + 80
    
    painter.goto(x,y)
    painter.pendown()
    painter.forward(50)
    y = y + 5

wn = trtl.Screen()

wn.mainloop()