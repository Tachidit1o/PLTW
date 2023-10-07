import turtle as trtl

painter = trtl.Turtle()
painter.turtlesize(9)
painter.pensize(3)
painter.forward(100)
painter.right(40)

methodes_and_attributes = dir(painter)
"""
for index, item in enumerate(methodes_and_attributes):
    print(f"Index {index}: {item}")
"""

for item in enumerate(methodes_and_attributes):
    print(item)

wn = trtl.Screen()
wn.mainloop()

