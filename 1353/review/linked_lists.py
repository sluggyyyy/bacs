def delete_second(self):
    first_node = self.head.next
    second_node = first_node.next
    
    if second_node is not None and second_node is not self.tail:
        third_node = second_node.next
        
        first_node.next = third_node
        third_node.prev = first_node
        
        self.size -= 1
        return second_node.value
        
def delete_second_to_last(self):
    last_node = self.tail.prev
    second_to_last_node = last_node.prev
    
    if second_to_last_node is not None and second_to_last_node is not self.head:
        third_node = second_to_last_node.prev
        
        last_node.prev = third_node
        third_node.next = last_node
        
        self.size -= 1
        return second_to_last_node.value
    
def mystery(self):
    current = self.head
    if current.next.next is not None:
        current = current.next
    current.next = current.next.next
    
def second_to_last_sll(self):
    if self.head is None or self.head.next is None:
        raise ValueError("List does not have a second-to-last node.")
    
    current = self.head
    if current.next.next.next is not None:
        current = current.next
    current.next = current.next.next