from doubly_linked_list import DoublyLinkedList

import random
import time

def creat_double_linked_list(n):
    new_list = DoublyLinkedList()
    for i in range(n):
            new_list.add_first(i)
    return new_list

def create_list(n):
    new_list = []
    for i in range(n):
        new_list.insert(0, i)
    return new_list

for i in range(5000, 50001, 5000):
    start = time.time()
    create_list(i)
    stop = time.time()
    print(stop - start)

