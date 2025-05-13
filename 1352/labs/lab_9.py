from random import randint, seed
## TODO: create a class called Box, which should include the following
class Box:
    def __init__(self, length: float = 0, width: float = 0, height: float = 0):
        self.length = length
        self.width = width
        self.height = height
# Implement a __str__ method, the data should be formatted, for example, as "2x5x10" (no spaces)
# (in the order length x width x height)
    def __str__(self):
        return f'{self.length}x{self.width}x{self.height}'
# Implement a __repr__ method, that simply calls __str__, and returns the value it returns.
    def __repr__(self):
        return self.__str__()
# (implementing __repr__ allows us to print a list of Box objects)
# Implement a volume method that returns the volume of the box.
    def volume(self):
        return self.length * self.width * self.height
# Implement an __eq__ method that returns true if the volume of the two boxes are identical.
    def __eq__(self, other):
        return self.volume() == other.volume()
    
    def __gt__(self, other):
        return self.volume() > other.volume()
    
    def __lt__(self, other):
        return self.volume() < other.volume()
    
    def __ge__(self, other):
        return self.volume() >= other.volume()
    
    def __le__(self, other):
        return self.volume() <= other.volume()
# Implement methods for <, >, <= and >=, using the volume to determine order of two boxes.

# The code in this main block tests your class. Do not modify anything in this method
# prior to the comment with TODO
def main():
    box1 = Box()
    box2 = Box(1, 2, 3)
    box3 = Box(2, 1, 3)
    box4 = Box(5, 4, 2)
    box5 = Box(5, 10, 0.8)
    print(box1, box2, box3, box4, box5)
    if box1.volume()==0:
        print("Passed test of default initialization values")
    else:
        print("Failed test of default initialization values")
    if not (box2 == box1 and box2==box3):
        print("Passed test of __eq__")
    else:
        print("Failed test of __eq__")
    if box1 < box2:
        print("Passed test of __lt__")
    else:
        print("Failed test of __lt__")  
    if box2 <= box3:
        print("Passed test of __le__")
    else:
        print("Failed test of __le__")
    if box4 != box5:
        print("Failed second test of __eq__")
    else:
        print("Passed second test of __eq__")
    if box4 > box1:
        print("Passed test of __gt__")
    else:
        print("Failed test of __gt__")   
    if box3 >= box4:
        print("Failed test of __ge__")
    else:
        print("Passed test of __ge__")
        
    # create a list of 100 random-sized boxes (don't edit this code)
    seed(91434000)
    boxes = [Box(randint(1,10), randint(1,10), randint(1,10)) for _ in range(100)]
    print(boxes)
    
    # TODO: write code to find the index of the box with the biggest volume in the list just
    # created. Use "<" to compare the sizes of the boxes. Store the index of the box with the
    # largest volume in a variable called index_of_max
    max_box = Box(0, 0, 0)
    index_of_max = 0
    for box in boxes:
        if box > max_box:
            max_box = box
            index_of_max = boxes.index(max_box)
    print(index_of_max)


    # Output the index of the box with largest volume (do not edit this line)
    # print(index_of_max)


if __name__ == "__main__":
    main()

