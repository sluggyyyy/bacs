import time

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.array = [None] * self.capacity
        
    def __str__(self):
        result = "["
        for i in range(self.size):
            result += str(self.array[i]) + ", "
        result += "]"
        return result
    
    def __len__(self):
        return self.size
    
    def set(self, i, e):
        if i < self.size:
            self.array[i] = e
        else:
            raise ValueError("Index out of bounds")
    
    def get(self, i):
        if i < self.size:
            return self.array[i]
        else:
            raise ValueError("Index out of bounds")
    
    def remove(self, i):
        if i < self.size:
            self.array.remove(self.array[i])
            self.size -= 1
        else:
            raise ValueError("Index out of bounds")
    
    def insert(self, i, e):
        if i < self.size:
            self.array.insert(i, e)
            self.size += 1
        else:
            raise ValueError("Index out of bounds")
    
    def expand_array(self):
        print("Array Expansion")
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
    
    def append(self, element):
        if self.size == self.capacity:
            self.expand_array()
        self.array[self.size] = element
        self.size += 1
        
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
class ArrayListArithmetic(ArrayList):
    def expand_array(self):
        new_array = self.array + ([None] * 1000)
        self.array = new_array
        self.capacity = len(self.array)
        
print(f'n\t\telapsed time\t\truntime')
num_trials = 10
for n in (100000, 200000, 400000, 800000):
    start = time.time()
    for i in range(num_trials):
        array_list = ArrayListArithmetic()
        for j in range(n):
            array_list.append(j)
    stop = time.time()
    print(f"{n}\t\t{stop - start}\t{(stop - start)/num_trials}")