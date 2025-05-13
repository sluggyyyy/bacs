class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__
    
    def __eq__(self, other) -> bool:
        return self.data == other.data

class DoublyLinkedList:
    def __init__(self):
        self.header = Node()
        self.tailer = Node()
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = 0

    def add_first(self, value):
        self.add_between(None, self.header.next.data, value)
 
    def add_last(self, value):
        new_node = Node(value)
        temp_node = self.tailer.prev
        new_node.prev = temp_node
        temp_node.next = new_node
        self.tailer.prev = new_node
        new_node.next = self.tailer
        self.size += 1

    def add_between(self, target1, target2, value):
        newNode = Node(value)
        current = self.header
        while current is not self.tailer:
            if current.data == target1:
                if current.next.data == target2:
                    nextNode = current.next
                    current.next = newNode
                    newNode.prev = current
                    newNode.next = nextNode
                    nextNode.prev = newNode
                    self.size += 1
                    return
            current = current.next
        raise ValueError("target data not found")
    
    def __str__(self) -> str:
        value = "[ "
        #Iterating through the list
        current = self.header.next
        while current is not self.tailer:
            value = value + str(current) + " "
            current = current.next
        value += "]"
        return value
    
    def __repr__(self) -> str:
        return self.__str__
        
    def __iter__(self):
        current = self.header.next
        while current is not self.tailer:
            yield current.data
            current = current.next

    def remove_between(self, target1, target2):
        current = self.header.next  # Start from the first actual element
        while current is not self.tailer:
            if (current.prev.data == target1) and (current.next.data == target2):
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next
        raise ValueError("No such element between the specified targets")

    def remove_value(self, value):
        pass
    
    def remove(self,value):
        current = self.head.next
        while current != self.tail:
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next
        raise ValueError("Value not found in list")