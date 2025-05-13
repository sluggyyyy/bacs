from singly_linked_list import SinglyLinkedList

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
        
    def peek(self):
        if self.is_empty():
            return None
        return self.stack.get_first()
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.remove_first()
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)