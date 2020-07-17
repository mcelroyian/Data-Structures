import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
from singly_linked_list import *

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Stack:
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

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if not self.storage.is_empty() and self.__len__() > 1:
            return self.storage.remove_tail()
        elif self.__len__() == 1:
            return self.storage.remove_head()
        else:
            return None


# Array Impl
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage[:0] = [value]

#     def pop(self):
#         if self.storage:
#             return self.storage.pop(0)
#         else:
#             return None
