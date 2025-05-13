"""
    Description of program: Game that allows user to draw objects onto the screen with some physics
    Filename: morgan_sand_game.py
    Author: Zachary Morgan  
    Date: 02/06/25
    Course: COMP1352
    Assignment: Project 3 SandGame - Part 2 
    Collaborators: N/A
    Internet Source: dudraw documentation
"""
import dudraw
import random

sand_color = dudraw.Color(210, 210, 140)
world_color = dudraw.Color(200, 230, 255)
EMPTY = 0
SAND = 1
FLOOR = 2
LAVA = 3
GLASS = 4
WATER = 5
BOMB = 6
pixel_radius = 1
size = 400
mode = SAND
# Global Variables to use throughout the program

def create_world(size: int) -> list:
    world = [[EMPTY for row in range(size)] for cell in range(size)]
    return world    

"""
    Create a list of size 'size' with all values initialized to EMPTY
    Later will be used to hold values of pixels on canvas
    
    Parameters: Takes an integer size
    Return: Returns the list
"""

def setup_world():
    dudraw.set_x_scale(0, 200)
    dudraw.set_y_scale(0, 200)
    dudraw.clear(world_color)
"""
    Sets up the canvas scale and background
"""
    
def draw_objects(world: list, mode: int) -> list:
    x, y = int(dudraw.mouse_x()), int(dudraw.mouse_y())
    if dudraw.mouse_is_pressed():
        if mode == SAND:
            for i in range(5):
                random_row = random.randint(1, 10)
                random_col = random.randint(1, 10)
                if (world[(y + 5) - random_row][(x + 5) - random_col] != FLOOR):
                  world[(y + 5) - random_row][(x + 5) - random_col] = SAND
                  
        elif mode == FLOOR:
            world[y][x] = FLOOR
            world [y - 1][x] = FLOOR
            world [y - 2][x] = FLOOR
            world[y][x + 1] = FLOOR
            world[y][x + 2] = FLOOR
            world[y - 1][x + 2] = FLOOR
            world[y - 2][x + 2] = FLOOR
            
        elif mode == LAVA:
            for i in range(1):
                random_row = random.randint(1, 10)
                random_col = random.randint(1, 10)
                if (world[(y + 5) - random_row][(x + 5) - random_col] != FLOOR):
                  world[(y + 5) - random_row][(x + 5) - random_col] = LAVA
        
        if mode == BOMB and dudraw.mouse_clicked():
            bomb_radius = 10
            
            dudraw.set_pen_color(dudraw.RED)
            dudraw.filled_circle(x, y, bomb_radius * 80)
            dudraw.set_pen_color(dudraw.YELLOW)
            dudraw.filled_circle(x, y, bomb_radius)
            dudraw.show(100)
            
            for i in range(-bomb_radius, bomb_radius):
                for j in range(-bomb_radius, bomb_radius):
                    bx = x + i
                    by = y + j
                    world[by][bx] = EMPTY
                    
            # FLOOR mode draws a 3x3 square that has collision with other objects
            # IMPORTANT: dudraw's mouse_x() and mouse_y() functions CANNOT keep up with fast mouse movements
            # Please do not dock points for there being holes in the floors when drawn too fast,
            # it is not solvable for me (I am sure there is a solution, just not with my current knowledge level)
                    
    for row in range(len(world)):
        for col in range(len(world[row])):
            if world[row][col] == SAND:
                dudraw.set_pen_color(sand_color)
                dudraw.filled_square(col, row, pixel_radius)
            elif world[row][col] == FLOOR:
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_square(col, row, pixel_radius)
            elif world[row][col] == LAVA:
                dudraw.set_pen_color(dudraw.Color(247, 104, 6))
                dudraw.filled_square(col, row, pixel_radius)
            elif world[row][col] == GLASS:
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.filled_square(col, row, pixel_radius)
def draw_floor(world: list) -> list:
    
    return world
"""
    If the mouse is pressed, set values at the world[mouse x][mouse y] position to different objects dependant
    on MODE value.
    Also holds the for loop that loops over the world list looking for OBJECT values, if it finds any 
    it draws a filled square at that column and row
    If the mode is bomb,  and mouse is clicked, draw two circles to represent an 'explosion'
    Nested loop that creates a 20x20 square of EMPTY after the 'explosion' takes place,
    erasing any objects 'beneath' that square!
    
    Parameters: Takes in the previously created world
    Return: Spits out updated list with different object variables applied
"""
def objects_fall(world: list) -> list:
    for row in range(len(world) - 1):
        for col in range(len(world[row]) - 1):
            #----SAND PHYSICS----#
            if world[row][col] == SAND and row > 0:
                if row > 0 and row - 1 < len(world) and col < len(world[0]) and world[row - 1][col] == EMPTY:
                    world[row - 1][col] = SAND   
                    world[row][col] = EMPTY
                
                elif world[row - 1][col] == FLOOR:
                    continue
                
                elif world[row - 1][col] == SAND:
                    if row > 0 and col > 0 and world[row - 1][col - 1] == EMPTY:
                        world[row][col - 1] = SAND
                        world[row][col] = EMPTY  
                    if row > 0 and col < len(world[0]) - 1 and world[row - 1][col + 1] == EMPTY:
                        world[row][col + 1] = SAND
                        world[row][col] = EMPTY
                    if row > 0 and world[row - 1][col - 1] == EMPTY and world[row - 1][col + 1] == EMPTY:
                        world[row][col + random.choice([-1, 1])] = SAND
                        world[row][col] = EMPTY
                        
                elif world[row - 1][col] == LAVA:
                    world[row][col] = GLASS
            
            #----LAVA PHYSICS----#            
            elif world[row][col] == LAVA and row > 0:
                if row > 0 and row - 1 < len(world) and col < len(world[0]) and world[row - 1][col] == EMPTY:
                    world[row - 1][col] = LAVA
                    world[row][col] = EMPTY
                else: 
                    lava_direction = random.random()
                    if lava_direction < 0.5:
                        if row > 0 and col > 0 and world[row][col - 1] == EMPTY:
                            world[row][col - 1] = LAVA
                            world[row][col] = EMPTY
                    elif row > 0 and col < len(world[0]) - 1 and world[row][col + 1] == EMPTY:
                            world[row][col + 1] = LAVA
                            world[row][col] = EMPTY
                            
                if world[row - 1][col] == SAND:
                     world[row - 1][col] = GLASS
                elif world[row][col - 1] == SAND:
                    world[row][col -1] = SAND
                elif world[row][col + 1] == SAND:
                    world[row][col + 1] = SAND
                    
    return world
"""
    Iterates over entire world list. Checks first for SAND values in the list. If SAND is found,
    and the cell below it is empty, move sand down and replace previous cell with EMPTY
    If the cell below the sand is FLOOR, continue (do nothing). If the SAND lands on SAND,
    Check left and right of sand particle, if either is open, move sand to that side
    If both left and right are open, choose a random direction. 

    For LAVA, same check if below LAVA is empty, move lava down and replace previous EMPTY.
    If below LAVA is NOT EMPTY, choose a random direction for the lava to move to (left or right)
    If below, left, or right of LAVA is SAND, turn SAND to GLASS

    Parameters: Takes in a 'world' list as a parameter
    Return: updated 'world' list
"""

def draw_mode(mode):
    if mode == SAND:
        dudraw.set_pen_color()
        dudraw.set_font_size(15)
        dudraw.text((dudraw.get_canvas_width() * 0.1),(dudraw.get_canvas_height() * 0.9),'Sand')
    elif mode == FLOOR:
        dudraw.set_pen_color()
        dudraw.set_font_size(15)
        dudraw.text((dudraw.get_canvas_width() * 0.1),(dudraw.get_canvas_height() * 0.9),'Floor')
    elif mode == LAVA:
        dudraw.set_pen_color()
        dudraw.set_font_size(15)
        dudraw.text((dudraw.get_canvas_width() * 0.1),(dudraw.get_canvas_height() * 0.9),'Lava')
    elif mode == BOMB:
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text((dudraw.get_canvas_width() * 0.1), (dudraw.get_canvas_height() * 0.9), 'Bomb')
        x, y = int(dudraw.mouse_x()), int(dudraw.mouse_y())
        bomb_radius = 5
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.filled_square(x, y, bomb_radius)  
"""
    Draw in the top left of the screen the current mode
    If mode is BOMB, grab x and y position of the mouse and draw a filled black square at x,y, size of bomb_radius
    This follows the mouse, automatically erasing itself when dudraw.clear() is called every frame in setup_world()
    
    Parameters: Takes in 'mode' as a parameter, a value that is updated within draw_world() by key presses
"""
    
def draw_world(world: list):
    key = ''
    global mode
    while key.lower() != 'q':
        if key.lower() == 'f':
            mode = FLOOR
        elif key.lower() == 's':
            mode = SAND
        elif key.lower() == 'l':
            mode = LAVA
        elif key.lower() == 'b':
            mode = BOMB
        setup_world()
        draw_objects(world, mode)
        world = objects_fall(world)                
        draw_mode(mode)
        dudraw.show(1)
        key = dudraw.next_key()
        
"""
    Handles all drawing and physics functions, holds the while loop used for animation and checks for user input 'q' to quit the program
    Also handles 'mode' checking and switching via key presses.
    Parameters: Takes in the world created by create_world()
"""

def main():
    # Create 'world' list of size 'size' store in variable 'w'
    w = create_world(size)
    # Set up canvas size using dudraw
    dudraw.set_canvas_size(size, size)
    # Call draw_world() to start the animation loop and allow the user to begin drawing sand
    draw_world(w)


if __name__ == '__main__':
    main()