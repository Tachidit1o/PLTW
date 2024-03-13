import turtle
import random

# Function to create a turtle with a random color and shape
def create_turtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(random.choice(["red", "blue", "green", "orange", "purple"]))
    t.speed(1)
    return t

# Function to move a turtle randomly
def move_random(t):
    angle = random.randint(0, 360)
    distance = random.randint(10, 50)
    t.left(angle)
    t.forward(distance)

# Main function
def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.title("Multiple Moving Objects")

    # Create multiple turtles
    num_turtles = 5
    turtles = [create_turtle() for L in range(num_turtles)]

    # Move the turtles randomly
    while True:
        for t in turtles:
            move_random(t)

    # Keep the window open until manually closed
    turtle.mainloop()

if __name__ == "__main__":
    main()
