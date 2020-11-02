import turtle
import random

# Create a new turtle and set its speed.
def turtle_setup(speed = 0):
    new_turtle = turtle.Turtle()
    new_turtle.speed(speed)
    return new_turtle

# Ask the user to select drawing choice and validate the entry.
def prompt_user(choices):
    invalid_choice = True

    print("Drawing Options:")
    for index in range(len(choices)):
        print(f"{index+1}) {choices[index]}")

    while invalid_choice:
        selection = input("Enter the number of your choice: ")
        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(choices):
            print("Invalid entry.")
        else:
            invalid_choice = False

    return int(selection)

# Place the turtle on the screen at the given x_pos and y_pos coordinates.
def move_turtle(trtl, x_pos, y_pos):
    trtl.penup()
    trtl.goto(x_pos, y_pos)
    trtl.pendown()

# Draw a regular polygon with the given number of sides.
def draw_reg_polygon(trtl_obj, num_sides, side_length):
    turn_angle = 360.0/num_sides
    for side in range(num_sides):
        trtl_obj.forward(side_length)
        trtl_obj.left(turn_angle)

# Draw a spirograph by rotating the turtle through an angle that does NOT go
# into 360° evenly.
def spirograph(trtl, diameter=200, angle=170):
    trtl.clear()
    move_turtle(trtl, -diameter/2, 0)
    trtl.color('purple', 'gold')
    trtl.begin_fill()
    for line in range(int(360/(180 - angle))):
        trtl.forward(diameter)
        trtl.left(angle)
    trtl.end_fill()
    trtl.hideturtle()

# Draw a series of polygons sharing one corner, but rotated around a central
# point.
def multi_polygon_spirograph(trtl, diameter=100, angle=170, sides=4):
    trtl.clear()
    move_turtle(trtl, 0, 0)
    trtl.color('navy', 'orange')
    trtl.begin_fill()
    for shape in range(int(360/(180 - angle))):
        draw_reg_polygon(trtl, sides, diameter)
        trtl.left(angle)
    trtl.end_fill()
    trtl.hideturtle()

def main():
    bob = turtle_setup()
    window = turtle.Screen()
    window.setup(600, 600, 50)
    options = ["Line Spirograph", "Square Spirograph", "Random Polygon Spirograph"]

    # Keep the drawing space open until done.
    still_going = True
    while still_going:
        # Ask the user what shape to draw.
        choice = prompt_user(options)

        # Call the proper function based on the user's choice.
        if choice == 1:
            spirograph(bob)
        elif choice == 2:
            multi_polygon_spirograph(bob)
        else:
            num_sides = random.randint(3, 10)
            multi_polygon_spirograph(bob, 100, 150, num_sides)

        # Check to see if the user wants to stop.
        still_going = input("Draw again (y/n)? ").lower() == 'y'

if __name__ == "__main__":
    main()
