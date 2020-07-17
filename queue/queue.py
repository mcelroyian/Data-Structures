import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
from singly_linked_list import *

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        count = 0
        current = self.storage.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def enqueue(self, value):
        self.size +=1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if not self.storage.is_empty():
            self.size -=1
            return self.storage.remove_head()
        else:
            return None


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage[:0] = [value]

#     def dequeue(self):
#         if self.storage:
#             return self.storage.pop()
#         else:
#             return None
