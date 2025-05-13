class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
    def __str__(self):
        return str(self.data)
    
class CircularLinkedList:
    def __init__(self) -> str:
        self.cursor = None
        self.size = 0
        
    def add_after_cursor(self, value):
        new_node = Node(value)
        if self.cursor is None:
            self.cursor = new_node
            new_node.next = new_node
        else:
            next_node = self.cursor.next
            self.cursor.next = new_node
            new_node.next = next_node
            
        self.size += 1
        
    def remove_after_cursor(self):
        if self.cursor is None:
            raise ValueError("List is empty.")
        if self.cursor.next is self.cursor:
            self.cursor = None
        else:
            self.cursor.next = self.cursor.next.next
        self.size -= 1
        
    def delete_value_at_cursor(self):
        if self.cursor is None:
            raise ValueError("Nothing in list.")
        else:
            deleted_node = self.cursor
            self.cursor = self.cursor.next
            last = self.cursor
            while last.next is not deleted_node:
                last = last.next
            last.next = self.cursor
            
    def advance_cursor(self, n):
        for i in range(0, n):
            self.cursor = self.cursor.next
            
    def get_value(self):
        if self.cursor is None:
            raise ValueError("empty list")
        else:
            return str(self.cursor.data)
    
    