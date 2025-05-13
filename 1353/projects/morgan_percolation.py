from random import random
import dudraw
from morgan_singly_linked_list import SinglyLinkedList
import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        self.stack = SinglyLinkedList()
    
    def get_size(self):
        return self.stack.get_size()
    
    def is_empty(self):
        return self.stack.get_size() == 0
    
    def __str__(self):
        return self.stack.__str__()
    
    def push(self, value):
        self.stack.add_first(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.remove_first()
    
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0

class Forest:
    def __init__(self, height, width, d):
        self.height = height
        self.width = width
        self.density = d
        
        forest = []
        
        for i in range(height):
            row = []
            for j in range(width):
                if random() <= self.density:
                    row.append(1)
                else:
                    row.append(0)
            forest.append(row)
        self.forest = forest
    
    def __str__(self):
        return str(self.forest)
    
    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.forest[i][j] == 1:
                    dudraw.set_pen_color(dudraw.GREEN)
                elif self.forest[i][j] == 0:
                    dudraw.set_pen_color_rgb(150, 75, 0)
                elif self.forest[i][j] == 2:
                    dudraw.set_pen_color(dudraw.RED)
                dudraw.filled_square(j, self.height - i - 1, 0.5)
                
    """
    # create a Stack cells_to_explore
    #set the top row of the forest on fire
    #for each cell (row and column) that is tree in the top row:
    mark the cell on fire
    add cell to cells_to_explore

    #continue lighting neighbors on fire
    As long as cells_to_explore is not empty
    pop the stack into current_cell
    if current_cell is on the bottom row then the fire spreads and we should return true
    for each neighboring tree cell
        mark the cell on fire
        push cell onto the stack

    #must not have reached the bottom row...
    return false
    """
    
    def depth_first_search(self):
        cells_to_explore = Stack()
        for i in range(self.width):
            if self.forest[0][i] == 1:
                self.forest[0][i] = 2
                cells_to_explore.push((0, i))
        while not cells_to_explore.is_empty():
            current_cell = cells_to_explore.pop()
            row = current_cell[0]
            col = current_cell[1]
            
            if row == self.height - 1:
                return True
            
            row_possibilities = [-1, 1, 0, 0]
            col_possibliities = [0, 0, -1, 1]

            for i in range(4):
                neighbor_row = row + row_possibilities[i]
                neighbor_col = col + col_possibliities[i]
                if 0 <= neighbor_row < self.height and 0 <= neighbor_col < self.width:
                    if self.forest[neighbor_row][neighbor_col] == 1:
                        self.forest[neighbor_row][neighbor_col] = 2
                        cells_to_explore.push((neighbor_row, neighbor_col))
        return False
    
    """
    # create a Queue cells_to_explore
    #set the top row of the forest on fire
    #for each cell (row and column) that is tree in the top row:
    mark the cell on fire
    add cell to cells_to_explore

    #continue lighting neighbors on fire
    As long as cells_to_explore is not empty
    dequeue the queue into current_cell
    if current_cell is on the bottom row then the fire spreads and we should return true
    for each neighboring tree cell
        set the cell on fire
        enqueue cell onto the queue

    #must not have reached the bottom row...
    return false
    """
    
    def breadth_first_search(self):
        cells_to_explore = Queue()
        for i in range(self.width):
            if self.forest[0][i] == 1:
                self.forest[0][i] = 2
                cells_to_explore.enqueue((0, i))

        while not cells_to_explore.is_empty():
            current_cell = cells_to_explore.dequeue()
            row, col = current_cell
            
            if row == self.height - 1:
                return True
            
            row_possibilities = [-1, 1, 0, 0]
            col_possibilities = [0, 0, -1, 1]

            for i in range(4):
                neighbor_row = row + row_possibilities[i]
                neighbor_col = col + col_possibilities[i]
                if 0 <= neighbor_row < self.height and 0 <= neighbor_col < self.width:
                    if self.forest[neighbor_row][neighbor_col] == 1:
                        self.forest[neighbor_row][neighbor_col] = 2
                        cells_to_explore.enqueue((neighbor_row, neighbor_col))
        return False

class FireProbability:
    def probability_of_fire_spread_dfs(d):
        fire_spread_count = 0
        
        for i in range(1000):
            f = Forest(20, 20, d)
            if f.depth_first_search():
                fire_spread_count += 1
        
        return fire_spread_count / 1000

    def probability_of_fire_spread_bfs(d):
        fire_spread_count = 0
        
        for i in range(1000):
            f = Forest(20, 20, d)
            if f.breadth_first_search():
                fire_spread_count += 1
                
        return fire_spread_count / 1000

    def highest_density_dfs():
        low_density = 0.0
        high_density = 1.0
        
        for i in range(20):
            density = (high_density + low_density) / 2.0
            p = FireProbability.probability_of_fire_spread_dfs(density)
            
            if p < 0.5:
                low_density = density
            else:
                high_density = density
                
        return density
    
    def highest_density_bfs():
        low_density = 0.0
        high_density = 1.0
        
        for i in range(20):
            density = (high_density + low_density) / 2.0
            p = FireProbability.probability_of_fire_spread_bfs(density)
            
            if p < 0.5:
                low_density = density
            else:
                high_density = density
                
        return density
    
    def graph():
        density = [i / 100 for i in range(101)]
        dfs_probabilities = []
        for d in density:
            dfs_probabilities.append(FireProbability.probability_of_fire_spread_dfs(d))
        
        bfs_probabilities = []
        for d in density:
            bfs_probabilities.append(FireProbability.probability_of_fire_spread_bfs(d))
        
        fig, ax = plt.subplots()
        ax.plot(density, dfs_probabilities, label="dfs")
        ax.plot(density, bfs_probabilities, label="bfs")
        ax.set_xlabel("density")
        ax.set_ylabel("prob")
        ax.legend()
        ax.grid(True)
        plt.show()
                    
def main():
    print(FireProbability.highest_density_dfs())
    print(FireProbability.highest_density_bfs())
    FireProbability.graph()
    
if __name__ == "__main__":
    main()
    
    
    