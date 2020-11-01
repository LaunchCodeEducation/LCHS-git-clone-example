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

def main():
    bob = turtle_setup()
    window = turtle.Screen()
    window.setup(600, 600, 50)

if __name__ == "__main__":
    main()