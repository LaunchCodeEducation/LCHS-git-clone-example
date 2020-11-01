import turtle
import random

def turtle_setup():
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    return new_turtle

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

if __name__ == "__main__":
    main()