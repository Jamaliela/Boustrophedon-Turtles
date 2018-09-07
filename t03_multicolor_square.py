######################################################################
# Author: Scott Heggen & Emily Lovell   TODO: Change this to your name, if modifying
# Username: heggens & lovelle           TODO: Change this to your username, if modifying
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# original from http://openbookproject.net/thinkcs/python/english3e/functions.html
#
# Modifications by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def draw_multicolor_square(t, sz):
    """
    Creates a multicolor square

    :param t: a Turtle object
    :param sz: size of a side of a square
    :return: None (void function)
    """
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)


def main():
    """
    Makes a multicolored spiralling set of squares

    :return: None
    """

    wn = turtle.Screen()        # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    wn.title("Dancing Squares!")

    tess = turtle.Turtle()      # Create tess and set some attributes
    tess.pensize(3)

    size = 20                   # Size of the smallest square
    for i in range(15):
        draw_multicolor_square(tess, size)  # Calls this function each iteration of the loop
        size = size + 10        # Increase the size for next iteration
        tess.forward(10)        # Move tess along a little
        tess.right(18)          # and give her some turn

    wn.exitonclick()


main()                          # Calls the main function
