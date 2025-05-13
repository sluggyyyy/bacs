import random

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.data)

class DoublyCircularLinkedList:
    def __init__(self) -> str:
        self.cursor = None
        self.size = 0
        
    def add_after_cursor(self, v):
        new_node = Node(v)
        if self.cursor is None:
            self.cursor = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:    
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            self.cursor.next = new_node
            new_node.next.prev = new_node
        self.size += 1
        
    def __str__(self):
        if self.cursor is None:
            return '[]'
        list_string = '['
        for i in range(self.size):
            list_string += str(self.cursor) + " " 
            self.cursor = self.cursor.next
        return list_string + "]"
    
    def advance_cursor(self, n):
        current = self.cursor
        for i in range(n):
            current = current.next
        self.cursor = current
        
    def get_value(self):
        return self.cursor.data
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def delete_cursor(self):
        if self.cursor is None:
            raise ValueError("List is empty")
        else:
            deleted_node = self.cursor
            self.cursor = deleted_node.next
            first = deleted_node.next
            last = deleted_node.prev
            first.prev = last
            last.next = first
            self.size -= 1
            return deleted_node.data
    
def homework_driver():
    random.seed(5)
    test_list = DoublyCircularLinkedList()

    for i in range(10):
        test_list.add_after_cursor(i)
    while not test_list.is_empty():
        n = random.randint(0,9)
        test_list.advance_cursor(n)
        print(test_list.delete_cursor(), end='')
    print()
homework_driver()
