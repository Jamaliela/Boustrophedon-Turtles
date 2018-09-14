#################################################################################
# Author: Ela Jamali, May Jue, Thomas Guthrie
# Username: Jamalie, Juem, Guthriet
#
# Assignment: T03: Boustrophedon turtles and functions
# Purpose: Drawing a square and painting the inside using loop and other functions
#################################################################################
# Attribution(s)
#################################################################################

import turtle      # allows us to use the turtle library


def draw_square(dis, ang):
    """
    We are making a square!
    :param dis: the distance that the turtle will move
    :param ang: the angle degree that we will turn left or right
    :return: None
    """
    square.forward(dis)   # we want the turtle to go forward
    for i in range(3):    # the repeatition
        square.right(ang)
        square.forward(dis)





def function_2():
    """
    Docstring for function_1
    """
    pass
    # ...


def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()                      # make a turtle screen
    wn.title("Ela & May & Thomas square")     # give the screen a title
    wn.color("lightgreem")                    # give it a color

    square = turtle.Turtle()
    square.pensize(20)
    square.color("purple")

main()
