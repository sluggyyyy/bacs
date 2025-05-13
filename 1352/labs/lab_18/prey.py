import dudraw
import random
from creature import Fish
class Minnow(Fish):
    """Small fish in the Lake"""
    MINNOW = dudraw.Color( 34, 168, 109 )
    def __init__(self, x, y):
        super().__init__(x,y,0)
        self.dead = False
    def __str__(self) :
        return f'{self.x},{self.y}, Reproduction value: {self.reproduce}'
    def __repr__(self) :
        return self.__str__()
    def is_dead( self ) :
        return self.dead
    def draw( self ) :
        dudraw.set_pen_color( Minnow.MINNOW )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )
    def move( self, lake ) :
        if self.dead :
            return
        # update reproduction level
        self.reproduce += 3
        # try to find a location where the minnow can move
        open_spaces = lake.check_adjacent_cells(self.x,self.y)
        # Minnows can only move to empty lake locations
        move_options = [k for k,v in open_spaces.items() if v is None]
        if len(move_options) > 0:
            move = random.choice(move_options)
            choice = random.randint(0, len(move_options) - 1)
            new_x = move_options[choice][0]
            new_y = move_options[choice][1]
            
            if self.reproduce >= 12:
                self.reproduce = 0
                lake.grid[self.x][self.y] = (Minnow(self.x, self.y))
            else:
                lake.grid[self.x][self.y] = None
            
            self.x = new_x
            self.y = new_y
            lake.grid[new_x][new_y] = self