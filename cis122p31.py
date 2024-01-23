'''
CIS 122 Spring 2022 Project 3-1
Author(s): Steven Sanchez-Jimenez
Credit: CIS 122 Resources only
Description: Sun and Earth Visualization
'''
from turtle import*

def main():

    '''this will be giving the positiona nd speed of the turle'''
    hideturtle()
    #this will hide the turtle so it is more visually appealing
    speed(10)
    #this is going to be the speed of the turtle when drawing
    penup()
    setpos(0,-200)
    pendown()
    # this codes above give the turtle a new beginning position
    return




def draw_vis():
    '''
    this will be the function to draw the sun and the earth
    '''
    sun_diameter = 1392000
    earth_diameter = 12756
    # ratio = 109/1
    r = sun_diameter/earth_diameter
    #the r stands for ratio
    r = r*2
    #i have doubled the ratio sizes of the sun and earth so they are more visible
    sun_diameter = r
    earth_diameter = 2
    print(sun_diameter , earth_diameter)
    #below, i will specify the colors for the circles
    color('yellow')
    begin_fill()
    circle(sun_diameter)
    end_fill()
    #the code above represents the circle of the sun
    color('blue')
    begin_fill()
    circle(earth_diameter)
    end_fill()
    return

def draw_sun_earth():
    sun_diameter = 1392000
    earth_diameter = 12756
    color('yellow')
    begin_fill()
    circle(sun_diameter)
    end_fill()
    color('blue')
    begin_fill()
    circle(earth_diameter)
    end_fill()




print(main(),draw_vis(), draw_sun_earth())







    


