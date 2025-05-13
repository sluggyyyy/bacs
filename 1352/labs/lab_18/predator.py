import dudraw
import random

from creature import Fish
import prey

class Trout(Fish):
    """Larger predatory fish in the Lake"""

    TROUT = dudraw.Color( 233, 110,  68)

    def __init__(self, x, y):
        # TODO: initialize this Trout using the parent class __init__
        #   also set energy for this Trout to 6
        super().__init__(x,y)
        self.energy = 6
    def __str__(self):
        # TODO: Produce a string representation of this Trout
        return f"The location of this trout is {self.x}, {self.y}"
    def __repr__(self):
        return self.__str__()

    def is_dead( self ):
        # TODO: This function should produce True if the Trout's energy is 0 or less
        if self.energy <= 0:
            return True
    def check_status(self,lake):
        # TODO: If this Trout is dead, set its lake grid location to None and
        #     add the Trout to the dead list so it can be removed later
        if self.is_dead():
            lake.grid[self.x][self.y] = None
            Fish.dead.append(self)

    def move(self, lake) :
        if self.is_dead() :
            return 
        
        # update the energy of the trout 
        self.energy -= 1

        open_spaces = lake.check_adjacent_cells(self.x,self.y)

        nearby_fish = [k for k,v in open_spaces.items() if isinstance(v, prey.Minnow)]
        if len(nearby_fish) > 0:
            choice = random.randint(0, len(nearby_fish) - 1)
            new_x = nearby_fish[choice][0]
            new_y = nearby_fish[choice][1]

            fish = lake.grid[new_x][new_y]
            fish.dead = True
            Fish.dead.append(fish)

            self.energy += 1
            self.reproduce += 0.5

            if self.reproduce >= 12:
                self.reproduce = 0
                lake.grid[self.x][self.y] = Trout( self.x, self.y )
            else:
                lake.grid[self.x][self.y] = None

            self.x = new_x
            self.y = new_y
            lake.grid[new_x][new_y] = self

        else:
            move_options = [k for k,v in open_spaces.items() if v is None]
            if len(move_options) > 0:
                choice = random.randint(0, len(move_options) - 1)
                new_x = move_options[choice][0]
                new_y = move_options[choice][1]

                if self.reproduce >= 12:
                    self.reproduce = 0
                    lake.grid[self.x][self.y] = Trout( self.x, self.y )
                else:
                    lake.grid[self.x][self.y] = None

                self.x = new_x
                self.y = new_y
                lake.grid[new_x][new_y] = self

    def draw( self ) :
        dudraw.set_pen_color( Trout.TROUT )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )