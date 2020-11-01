import turtle
import random

def turtle_setup():
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    return new_turtle

def main():
    bob = turtle_setup()
    window = turtle.Screen()
    window.setup(600, 600, 50)

if __name__ == "__main__":
    main()