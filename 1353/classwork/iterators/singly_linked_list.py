class SLLIterator:
    def __init__(self, start):
        self.current = start
        
    def __next__(self):
        if not self.current is None:
            result = self.current
            self.current = self.current.next
            return result
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self
        
class Node:
    def __init__(self, v, n = None):
        self.value = v
        self.next = n       
    def __eq__(self, other):
        return self.value == other.value   
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return self.__str__()
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        return SLLIterator(self.head)
    
    def get_size(self):
        return self.size
    
    def add_last(self, v):
        new_node = Node(v)
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
        self.size += 1
    
    def add_first(self, v):
        new_node = Node(v, self.head)
        self.head = new_node
        self.size += 1
        
    def __str__(self):
        if self.head is None:
            return " - "
        else:
            result = ""
            current = self.head
            while not current is None:
                result += str(current) + " "
                current = current.next
            return result
        
    def min(self):
        if self.head is None:
            raise ValueError
        else:
            current = self.head
            result = current.value
            while not current is None:
                if current.value < result:
                    result = current.value
                current = current.next
            return result
    
    def rotate(self, idx):
        if self.head is None or idx == 0:
            return
        
        prev = self.head
        for _ in range(idx - 1):
            if prev.next is None:
                raise ValueError("Value doesn't exist")
            prev = prev.next
        
        target = prev.next
        if target is None:
            raise ValueError("Value doesn't exist")
        
        prev.next = self.head
        temp = self.head.next
        self.head.next = target.next
        target.next = temp
        self.head = target
        
    def remove_at_index(self, index):
        if self.head is None or index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return

        prev = self.head
        for _ in range(index - 1):
            if prev.next is None:
                return
            prev = prev.next

        prev.next = prev.next.next
            
    def is_empty(self):
        self.head.next is None
    
    def remove_first(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp
    
    def remove_last(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        current.next = None
        
    def get(self, index):
        if self.head is None or index == 0:
            return
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current
    
sll = SinglyLinkedList()
sll.add_first(1)
sll.add_first(2)
sll.add_first(3)
sll.add_first(10)
sll.add_first(20)
it = sll.__iter__()

print("Method 2")
while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break
    
print("\nMethod 3")
for val in sll:
    print(val)