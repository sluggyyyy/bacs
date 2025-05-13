class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None    
        self.prev = None
    def __eq__(self, other):
        return self.value == other.value   
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
    
    def add_first(self, data):
        new_node = Node(data)
        next_node = self.head.next
        self.head.next = new_node
        new_node.next = next_node
        new_node.prev = self.head.next
        next_node.prev = new_node
        self.size += 1
        
    def add_last(self, data):
        new_node = Node(data)
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
        
    def add_between(self, target_value1, target_value2, new_value):
        current = self.head.next
        while current is not self.tail:
            if current.value == target_value1:
                if current.next.value == target_value2:
                    new_node = Node(new_value)
                    node1 = current
                    node2 = current.next
                    node1.next = new_node
                    new_node.prev = node1
                    new_node.next = node2
                    node2.prev = new_node
                    self.size += 1
                    return
            current = current.next
        raise ValueError("Target data not found")
                
    def remove_between(self, node1, node2):
        current = self.head
        while current.next is not None:     
            if current.value == node1:
                if current.next.next.value == node2:
                        return_value = current.next.value
                        temp = current.next.next
                        current.next = temp
                        temp.prev = current
                        return return_value
            current = current.next
        raise ValueError("Target Value not found")
         
    def remove_first(self):
        self.remove_between(self.head.value, self.head.next.next.value)
    
    def remove_last(self):
        self.remove_between(self.tail.prev.prev.value, self.tail.value)
        
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1