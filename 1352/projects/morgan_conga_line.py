from __future__ import annotations
import dudraw
import random

"""
    Description of program: Implementation of dancer class used to move 
    "dancer" objects in a way that follows other dancers
    
    Filename: morgan_conga_line.py
    Author: Zachary Morgan  
    Date: 02/14/25
    Course: COMP1352
    Assignment: Project 4 - Lists of objects (Conga Line)
    Collaborators: N/A
    Internet Source:
"""

class Dancer:
    def __init__(self, x = 0, y = 0, r = 0.025):
        self.x = x
        self.y = y
        self.radius = r
        
        # Initialize instance variables for x, y, radius
    
    def __str__(self):
        return f'{self.x} | {self.y} | {self.targetx} | {self.targety}'
    
        # Print instance coordinates and target coordinates for debugging
    
    def draw(self):
        dudraw.filled_circle(self.x, self.y, self.radius)
        
        # Draw a circle with instance variables x, y, and radius!
        
    def move(self):
        direction_x = self.targetx - self.x
        direction_y = self.targety - self.y
        self.x += direction_x * 0.005
        self.y += direction_y * 0.005
        
        # Calculates direction needed by subtracting coordinates of target
        # from coordinates of self, increments self by the direction multiplied
        # by a speed of 0.005
    
    def set_target(self, targetx, targety):
        self.targetx = targetx
        self.targety = targety
        
        # Takes in the coordinates of the target object and updates
        # target x and target y instance variables accordingly
        
def main():
    key = ''
    # Initialize string variable key
    dudraw.set_canvas_size(400, 400)
    # Set canvas size to arbitrary 400x400
    dancer_list = [Dancer(random.random() * 1, random.random() * 1, random.uniform(0.005, 0.01)) for _ in range(12)]
    # Create dancer list with default 12 dancers with random initial 
    # coordinates and random radius
    while key.lower() != 'q':
    # Check if q is pressed, if it is, program will terminate
        dudraw.clear(dudraw.LIGHT_GRAY)
        # Clear the canvas
        for i in range(len(dancer_list)):
        # Iterate over dancer_list
            if i == 0:
            # If we are on the first Dancer in dancer_list...
                dancer_list[i].set_target(dudraw.mouse_x(), dudraw.mouse_y())
                # Set the target coordinates to be those of the mouse position
            else:
                dancer_list[i].set_target(dancer_list[i - 1].x, dancer_list[i - 1].y)
                # Else: set coordinates to be those of the object in front of 
                # current object in iteration
            dancer_list[i].move()
            # Update coordinates to new coordinates based off of calculations in Dancer.move()
            dancer_list[i].draw()
            # Draw the updated Dancer
            
        if key == 'n':
        # If 'n' key is pressed:
            dancer_list.append(Dancer(random.random() * 1, random.random() * 1, random.uniform(0.005, 0.01)))
            # Append a new Dancer to the end of the list
        dudraw.show(1)
        # Update canvas every 1ms
        key = dudraw.next_key()
        # Update key value with next key pressed

if __name__ == "__main__":
    main()