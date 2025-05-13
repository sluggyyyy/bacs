import dudraw
import random 

from creature import Fish
from prey import Minnow
from predator import Trout

class Lake:

    # Color for drawing Lake locations
    LAKE_COLOR = dudraw.Color(70, 70, 110)

    """The Lake is a grid of width by height locations. Each location is either empty (None) or a contains a fish"""
    def __init__(self, width, height) :
        self.width = width 
        self.height = height

        self.grid = []
        for x in range(0, width):
            self.grid.append([])
            for y in range(0, height):
                self.grid[x].append(None)
    
    def spawn_fish(self, fish_type):
        """Randomly choose beginning location of fishies."""
        spawned = False
        while not spawned:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[x][y] == None:
                spawned = True
        if fish_type == "minnow":
            self.grid[x][y] = Minnow(x, y)
        elif fish_type == "trout":
            self.grid[x][y] = Trout(x, y)

    def draw(self):
        """Draw the current minnows and trouts in the lake"""

        # TODO: Write nested for loops which iterate over the grid cells of the lake
        #    If the cell value is None, draw a lake square
        #    Otherwise the cell value is a fish object so ask the fish to draw itself
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j] == None:
                    self.draw_lake_cell(i, j)
                else:
                    self.grid[i][j].draw()
    
    def draw_lake_cell( self, x, y ) :
        dudraw.set_pen_color( Lake.LAKE_COLOR )
        dudraw.filled_rectangle( x+0.5, y+0.5, 0.45, 0.45 )

    def check_adjacent_cells(self, loc_x, loc_y):
        """
        Create dictionary of adjacent cell contents, 
        adjusting for horizontal and vertical wrap-around.
        Dictionary contents are either None (empty), or a Minnow or Trout object.
        """
        results = {}
        for x, y in [(loc_x + i, loc_y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
                # Check for wrap around on vertical coordinate
                if y == self.height:
                    y = 0
                elif y < 0:
                    y = self.height - 1

                # Check for wrap around on horizontal coordinate
                if x == self.width:
                    x = 0
                elif x < 0:
                    x = self.width - 1
                results[x,y] = self.grid[x][y]
        return results