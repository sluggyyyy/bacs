"""
Description of program: 
File Name: morgan_hw1.py
Date: 1/13/25
Course: COMP 1352
Assignment: Homework 1, debugging
Collaborators: 
Internet Sources: 
"""
"""    
    
1. Bug description: there is only one circle showing up, in the lower-left 
    corner, clipped, color black. 
    
2. Program Error (why is this behavior happening?):
    x_pos and y_pos (lines 34 and 35) use random.random() to generate a float from 0 to 1,
    typecasting this value to an int before multiplying by scale (which the program was doing initially)
    rounds the float down to 0, making all circles appear at 0,0
    
3. Solution:
    typecast to integer after multiplying by scale so that value is not being rounded down to 0
    
4. Small Fixes:
    - Missing semicolon on conditional statement
    - Improper indents on second if/elif statement group that was breaking positioning of circles
    by blocking last two if statements from ever being used
    - Removed useless count variable
    - Rearranged comments to reflect properly which sector was being colored
"""
import dudraw
import random

def main():
    size = 400   # pixel-size of the canvas
    scale = 100  # scale on both x-axis and y-axis
    dudraw.set_canvas_size(size, size)
    dudraw.set_x_scale(0, scale)
    dudraw.set_y_scale(0, scale)
    for i in range(10000):
        """
        old code:
        x_pos = int(random.random())*scale
        y_pos = int(random.random())*scale
        """
        x_pos = int((random.random())*scale)
        y_pos = int((random.random())*scale)
        # bottom left triangle - cyan
        if x_pos > y_pos and x_pos < scale/2:
            dudraw.set_pen_color_rgb(0, 255, 255)
        # lower right trapezoid - magenta
        elif x_pos > y_pos and x_pos >= scale/2:
            dudraw.set_pen_color_rgb(255, 0, 255)
        # top left trapezoid - green   
        if x_pos < y_pos and x_pos < scale/2:
                dudraw.set_pen_color_rgb(0, 255, 0)
        # upper right triangle - blue
        elif x_pos < y_pos and x_pos >= scale/2:
                dudraw.set_pen_color_rgb(0, 0, 255)

        dudraw.filled_circle(x_pos, y_pos, 2)
        dudraw.show(10)

if __name__ == "__main__":
    main()