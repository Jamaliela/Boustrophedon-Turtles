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


def draw_square(t, d):
    """
    We are making a square!
    :param t: The name of our turtle
    :param d: the distance it will move forward
    :return: None
    """
    t.forward(d)   # we want the turtle to go forward
    for i in range(3):    # the repeatition to create the 3 side of the square
        t.right(90)    #this is for turning
        t.forward(d)   #this is for moving forward

def filling_in_square(f, dis):
    """
    this is for filling in the square
    :param f: the turtle to fill in the square
    :param dis: the distance that the turtle will move
    :return: none
    """
    f.penup()       # turtle go into the square
    f.forward(dis)
    f.right(90)
    f.forward(dis)
    f.pendown()
    f.left(90)
    for i in range(11):         #the turtle is in loop to fill in the square
        f.forward(460)
        f.right(90)
        f.forward(dis)
        f.right(90)
        f.forward(460)
        f.left(90)
        f.forward(dis)
        f.left(90)

    f.forward(460)      #the turtle fill in the last two line
    f.right(90)
    f.forward(dis)
    f.right(90)
    f.forward(460)

    # ...


def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()                      # make a turtle screen
    wn.title("Ela & May & Thomas square")     # give the screen a title
    wn.bgcolor("lightgreen")                    # give it a color

    square = turtle.Turtle()        #creating turtle to draw the square border
    square.pensize(20)
    square.color("purple")

    square.penup()              #setting up the turtle's position
    square.setpos(-250,250)
    square.pendown()

    fill = turtle.Turtle()          #creating the turtle for the fill in
    fill.pensize(20)
    fill.color("blue")

    fill.penup()                #setting up turtle position for the fill in square
    fill.setpos(-250,250)

    distance = 500
    dis = 20


    draw_square(square, distance)       #creating directory for the def
    filling_in_square(fill, dis)

    wn.exitonclick()

main()
