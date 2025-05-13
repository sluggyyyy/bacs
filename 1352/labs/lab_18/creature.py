class Fish:
    """Base class for all Fish in the Lake"""

    # Class variables to hold all living fish and
    #   any dead fish before they are removed from the simulation
    living = []
    dead = []

    def __init__(self, x, y, reproduce=0):
        # TODO: Initialize x, y, and reproduce for this Fish
        self.x = x
        self.y = y
        self.reproduce = reproduce
        # TODO: Also add self to the list of living fish
        Fish.living.append(self)
    def __str__(self):
        # TODO: Produce a string representation of this Fish
        return f"This fish is located at {self.x},{self.y}."
    def __repr__(self):
        return self.__str__()
    
    def remove_dead_fish():
        # TODO: For every fish in the current dead list
        #    remove the fish from the living list
        #    then clear the dead list
        for dead_fish in Fish.dead:
            Fish.living.remove(dead_fish)
        Fish.dead.clear()
    
    def is_dead(self) :
        return False 

    def move(self, lake):
        pass

    def check_status(self, lake):
        pass

    def draw(self) :
        pass