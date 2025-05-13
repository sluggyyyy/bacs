"""
 Filename: bouncing_circle.py
 Author: 1352 instructors
 Date: January 2024
 Course: COMP 1352
 Assignment: animation demo, to be modified to use classes
 Collaborators: None
 Internet Source: None
"""
from __future__ import annotations
from random import random
import dudraw
from dudraw import Color
import math

class BouncingCircle:
    def __init__(self, x_position, y_position, x_velocity, y_velocity, radius):
        self.color = Color(int(random()*256), int(random()*256), int(random()*256))
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.radius = radius
        
    def move(self):
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity
        if (self.x_position > 1-self.radius and self.x_velocity > 0 or self.x_position < self.radius and self.x_velocity < 0):
            self.x_velocity *= -1
        if (self.y_position > 1-self.radius and self.y_velocity > 0 or self.y_position < self.radius and self.y_velocity < 0):
            self.y_velocity *= -1

    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.radius)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.x_position, self.y_position, self.radius)
    
    def overlaps(self, circ2: BouncingCircle):
        if math.sqrt((circ2.x_position - self.x_position) ** 2 + (circ2.y_position - self.y_position) ** 2) <= self.radius + circ2.radius:
            dudraw.set_font_size(50)
            dudraw.text(0.5, 0.5, "Crash!")
        
def main():
    dudraw.set_canvas_size(400,400)
    # create values to represent circle’s properties
    # animation loop, continue until user types ‘q’
    key = ''
    circle1 = BouncingCircle(random(), random(), 0.05*random(), 0.05*random(), 0.075)
    circle2 = BouncingCircle(random(), random(), 0.05*random(), 0.05*random(), 0.05)
    while key != 'q':
        dudraw.clear(dudraw.LIGHT_GRAY)
        circle1.draw()
        circle1.move()
        circle2.draw()
        circle2.move()
        circle1.overlaps(circle2)
        key = dudraw.next_key()
        # display the new frame and pause for 1/20 of a second
        dudraw.show(50)
if __name__== '__main__':
    main()