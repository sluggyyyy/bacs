import dudraw
import random

class Node:
    def __init__(self, v = None, x = 10, y = 10):
        self.value = v
        self.next = None    
        self.prev = None
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.value == other  
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return self.__str__()
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def add_first(self, data, x, y):
        new_node = Node(data)
        new_node.x = x
        new_node.y = y
        next_node = self.head.next
        self.head.next = new_node
        new_node.next = next_node
        new_node.prev = self.head
        next_node.prev = new_node
        self.size += 1
        
    def add_last(self, data, x, y):
        new_node = Node(data)
        new_node.x = x
        new_node.y = y
        temp_node = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail
        new_node.prev = temp_node
        temp_node.next = new_node
        self.size += 1
    
    def __str__(self):
        if self.head is None:
            return " - "
        else:
            result = ""
            current = self.head.next
            while current is not None and current is not self.tail:
                result += str([current]) + " "
                current = current.next
            return result
         
    def remove_first(self):
        if self.is_empty():
            raise ValueError ("List is empty")
        
        first_node = self.head.next
        second_node = first_node.next
        
        self.head.next = second_node
        second_node.prev = self.head
        
        self.size -= 1
        return first_node.value
    
    def remove_last(self):
        if self.is_empty():
            raise ValueError ("List is empty")
        
        last_node = self.tail.prev
        second_to_last_node = last_node.prev
        
        self.tail.prev = second_to_last_node
        second_to_last_node.next = self.tail
        
        self.size -= 1
        return last_node.value
        
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def is_empty(self):
        return self.head.next is self.tail
    
    def first(self):
        if self.head.next is not self.tail:
            return self.head.next.value
        
    def last(self):
        if self.head.next is not self.tail:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            return current.value
        
    def get(self, i):
        if self.head.next is not self.tail:
            current = self.head.next
            for _ in range(i):
                current = current.next
            return current.value
        
class Snake(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        
    def draw(self):
        # Loop over nodes starting with first node after head sentinel
        current = self.head.next
        while current is not None and current is not self.tail:
            # Draw black rectangles of size 1x1
            dudraw.set_pen_color(dudraw.GREEN)
            dudraw.filled_rectangle(current.x, current.y, 0.5, 0.5)
            # Advance to next node
            current = current.next
            
    def move(self, direction):
        # Create variables for head segment of snake, old_x, old_y
        current_head = self.head.next
        old_x = current_head.x
        old_y = current_head.y
        
        # Initialize variables to be edited by a value based on direction parameter
        new_x = old_x
        new_y = old_y
        
        # Direction handling
        if direction == 1: # Right
            new_x += 1
        elif direction == 2: # Up
            new_y += 1
        elif direction == 3: # Left
            new_x -= 1
        elif direction == 4: # Down
            new_y -= 1

        # Add a new segment in front of current head (last will be removed in main())
        self.add_first(0, new_x, new_y)
    
    def check_collision(self):
        if self.is_empty():
            return False
        
        # Keep track of head node and initialize current "index" starting with first node
        head_node = self.head.next
        current = head_node.next
        # Loop over entire list
        while current is not self.tail:
            # If head node x coord and y coord match any segment x,y return True, Bool return will be used for handling in main()
            if head_node.x == current.x and head_node.y == current.y:
                return True
            current = current.next
        return False     

class Food(Node):
    def __init__(self, x, y):
        # Initialize a food object, same as node but has x,y coords
        super().__init__()
        self.x = x
        self.y = y
        
    def draw(self):
        # Draw a red food!
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(self.x, self.y, 0.5, 0.5)
        
        
def main():
    # Start snake in middle of canvas
    start_x = 10
    start_y = 10
    
    # Instantiate a snake object
    snake = Snake()
    
    # Start with 3 segments
    snake.add_first(0, start_x, start_y - 2)
    snake.add_first(0, start_x, start_y - 1)
    snake.add_first(0, start_x, start_y)
    
    # Initialize canvas and clear it with color white
    dudraw.set_canvas_size(400, 400)
    # Scale offset by 0.5 so that the snake and food are all the way on screen at all times
    dudraw.set_scale(-0.5, 19.5)
    dudraw.clear(dudraw.DARK_GREEN)
    
    # Initialize game_over bool for game end handling
    game_over = False
    
    # Initialize number of food for food handling
    num_food = 0
    
    # Initialize score
    score = 0
    
    # Limit and timer for animation updating
    limit = 10
    timer = 0
    
    # Initialize direction starting going UP, init last direction too for 
    direction = 2
    last_direction = 2
    
    # Begin animation loop
    while True:
        if not game_over:
            # Initialize key variable taking input from keyboard
            key = dudraw.next_key()
            
            # Initialize new_direction, updated by following conditional
            new_direction = direction 
            # Prevent moving down if currently moving up
            if key == 'w' and last_direction != 4:
                new_direction = 2
            # Prevent moving up if currently moving down
            elif key == 's' and last_direction != 2: 
                new_direction = 4
            # Prevent moving right if currently moving left
            elif key == 'a' and last_direction != 1:
                new_direction = 3
            # Prevent moving left if currently moving right
            elif key == 'd' and last_direction != 3: 
                new_direction = 1
            # Update direction with new_direction value spit out by previous conditional
            direction = new_direction
        
        # If the game is not over
        if not game_over:
            # Update timer
            timer += 1
            # If timer == limit, reset timer and continue...
            if timer == limit:
                timer = 0
                
                # Keep track of current head
                current_head = snake.head.next
                # Keep track of head's coordinates
                head_x, head_y = current_head.x, current_head.y
                
                # If out of bounds, end game
                if head_x < 0 or head_x > 19 or head_y < 0 or head_y > 19:
                    game_over = True
                
                # Initialize ate_food boolean for handling snake growth
                ate_food = False
                
                # If food exists and head touches food...
                if num_food > 0 and food is not None and head_x == food.x and head_y == food.y:
                    # Update boolean
                    ate_food = True
                    # Update number of food
                    num_food -= 1
                    # Remove food
                    food = None
                
                if not game_over:
                    # Move the snake in the direction previously determined by the movement conditional
                    snake.move(direction)
                    
                    # Check for collision
                    if snake.check_collision():
                        # If collision, end game
                        game_over = True
                    
                    # If the snake did not eat food...
                    if not ate_food:
                        # Remove the last segment, head segment is updated inside of Snake.move()
                        snake.remove_last()
                        # This previous conditional does not activate if food was eaten, meaning a new segment will be added
                    
                    # Update score
                    if ate_food:
                        score += 1
                    
                    # Update last_direction for use in above conditional at beginning of next loop
                    last_direction = direction
        
        # Clear the canvas and draw the snake!           
        dudraw.clear(dudraw.DARK_GREEN)
        snake.draw()

        # If there is no food, create food
        if num_food < 1 and not game_over:
            food_x = random.randint(0, 19)
            food_y = random.randint(0, 19)
            food = Food(food_x, food_y)
            num_food += 1
        
        # If food exists, draw food
        if food is not None:
            food.draw()
        
        # Game over screen
        if game_over == True:
            center = (-0.5 + 19.5) / 2
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.set_font_size(24)
            dudraw.text(center, center, "Game Over")
            dudraw.set_font_size(16)
            dudraw.text(center, 8.25, f"Final Score: {score}")
        
        # Score tracker
        elif not game_over:
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.set_font_family('Courier')
            dudraw.set_font_size(12)
            dudraw.text(18, 19, f"Score: {score}")
        
        # Draw a new frame every 10ms
        dudraw.show(10)
        
if __name__ == "__main__":
    main()