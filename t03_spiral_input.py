######################################################################
# Author: Scott Heggen & Emily Lovell   TODO: Change this to your name, if modifying
# Username: heggens & lovelle           TODO: Change this to your username, if modifying
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Modifications by Dr. Jan Pearce, Dr. Mario Nakazawa, and Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def create_turtle():
    """
    A fruitful function for creating a turtle.

    :return: a Turtle object
    """
    stamper = turtle.Turtle()
    stamper.shape("circle")
    stamper.color("green")
    stamper.penup()                 # raise the pen so that we do not have a trail
    return stamper                  # returns a turtle to the line of code where this function was called


def stamp_thirty(tur, size_increase):
    """
    A function for stamping thirty dots to the screen using a turtle.

    :param tur: a Turtle object
    :param size_increase: how much to increase each iteration of the loop
    :return: None
    """
    size = 4                        # initial stride length
    for i in range(30):             # we are going to create 30 stamps
       tur.stamp()                  # Leave an impression on the canvas
       size = size + size_increase          # Increase the move distance on every iteration
       tur.forward(size)            # Move stamper along
       tur.right(34)                #  ...  and turn her


def main():
    """
    The main function of the program, where all things begin

    :return: None
    """
    win = turtle.Screen()
    increase_size = int(input("How much is the stride increase? "))
    miss_turtle = create_turtle()  # Calls the function that creates the turtle. Saves the output of that function to a variable called miss_Turtle
    stamp_thirty(miss_turtle, increase_size)
    win.exitonclick()


main()      # Invokes the main() function
