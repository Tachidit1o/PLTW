import turtle as trtl

painter = trtl.Turtle()
painter.turtlesize(9)
painter.pensize(3)
painter.left(90)

painter.forward(100)
painter.right(90)
painter.forward(100)

methodes_and_attributes = dir(painter)
"""
for index, item in enumerate(methodes_and_attributes):
    print(f"Index {index}: {item}")

Note: The above code is different than this: 

for item in enumerate(methodes_and_attributes):
    print(item)
"""



wn = trtl.Screen()
wn.mainloop()

