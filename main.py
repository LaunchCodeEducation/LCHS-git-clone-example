import turtle
import random

def turtle_setup():
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    return new_turtle

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

def move_turtle(trtl, x_pos, y_pos):
    trtl.penup()
    trtl.goto(x_pos, y_pos)
    trtl.pendown()

def draw_reg_polygon(trtl, sides, length):
    turn_angle = 360.0/sides
    for side in range(sides):
        trtl.forward(length)
        trtl.left(turn_angle)

def spirograph(trtl, diameter=200, angle=170):
    trtl.clear()
    move_turtle(trtl, -diameter/2, 0)
    trtl.color('red', 'yellow')
    trtl.begin_fill()
    for line in range(int(360/(180 - angle))):
        trtl.forward(diameter)
        trtl.left(angle)
    trtl.end_fill()
    trtl.hideturtle()

def multi_polygon_spirograph(trtl, diameter=100, angle=170, sides=4):
    trtl.clear()
    move_turtle(trtl, 0, 0)
    trtl.color('dark green', 'orchid')
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

    still_going = True
    while still_going:
        choice = prompt_user(options)

        if choice == 1:
            spirograph(bob)
        elif choice == 2:
            multi_polygon_spirograph(bob)
        else:
            num_sides = random.randint(3, 10)
            multi_polygon_spirograph(bob, 100, 150, num_sides)

        still_going = input("Draw again (y/n)? ").lower() == 'y'

if __name__ == "__main__":
    main()
