from singly_linked_list import SinglyLinkedList
import random

def homework_driver():
    random.seed(6)
    testing_list= SinglyLinkedList()
    for i in range(1,4):
        testing_list.add_first(i * random.randint(0,10))
        testing_list.add_last(i * random.randint(0,10))
        testing_list.add_first(i * random.randint(0,10))
        testing_list.add_last(i * random.randint(0,10))
    # print(TestingList)
    for _ in range(5):
        rand_index=random.randint(0,20)
        # print(f'rand_index is {rand_index}')
        try: testing_list.remove_at_index(rand_index)
        except IndexError as e:
            pass
            # print(e)
    print(testing_list)

#The following is the main code block:
homework_driver()
