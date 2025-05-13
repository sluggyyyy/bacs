import dudraw
import random 

from lake import Lake
from creature import Fish

# Constants for dudraw canvas size
CANVAS_X = 900
CANVAS_Y = 600

# Constants for width and height of simulation grid
WIDTH = 90
HEIGHT = 60

# Constant for the canvas background color
BACKGROUND = dudraw.Color(62, 70,  73)
       
def main():
    dudraw.set_canvas_size( CANVAS_X, CANVAS_Y )
    dudraw.set_x_scale( 0, WIDTH )
    dudraw.set_y_scale( 0, HEIGHT )

    # TODO: Create a lake object using WIDTH and HEIGHT
    the_lake = Lake(WIDTH, HEIGHT)

    # constant for number of time steps to run simulation
    chronons = 1000

    # constants for the starting numbers of fish in the lake
    num_minnows = 200
    num_trouts = 30

    # stock the lake with fish
    
    # TODO: Write a loop to add minnows to the lake using the spawn_fish method
    for i in range(num_minnows):
        the_lake.spawn_fish("minnow")
    # TODO: Write a loop to add trout to the lake using the spawn_fish method
    for i in range(num_trouts):
        the_lake.spawn_fish("trout")
    
    dudraw.clear(BACKGROUND)

    # Simulation loop
# Simulation loop
    running = True
    while running:
        if chronons > 0:
            # check for dead fish in the lake
            # TODO: Write a loop to check the status of all fish in the lake
            for row in the_lake.grid:
                for fish in row:
                    if fish is not None:
                        fish.check_status(the_lake)

            print(f"Living fish: {Fish.living}")
            print(f"Dead fish: {Fish.dead}")
            # move all fish in the lake
            # TODO: Write a loop to move all fish in the lake
            for row in the_lake.grid:
                for fish in row:
                    if fish is not None:
                        fish.move(the_lake)
            # remove all dead fish
                Fish.remove_dead_fish()
            # TODO: Write a line of code to draw the lake
            the_lake.draw()
            chronons -= 1
        dudraw.show( 10 )

if __name__ == '__main__':
    main()