"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create a ListNode with the passed in value
        new_node = ListNode(value)
        #If there is NOT a head
        if self.length == 0:
            #set the head and tail to new_node
            self.head = new_node
            self.tail = new_node 
            #update length +1
            self.length += 1

        #if there is a head
        else:
            old_head = self.head
            #1. reassign head field of the DoublyLinkedList Class
            self.head = new_node
            #2. new_node or current head's next value needs to
            #old head
            self.head.next = old_head
            old_head.prev = self.head
            #3. old head prev need to point to new head or new_node
  
            #4 update length +1
            self.length += 1


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #No existing head
        if not self.head:
            return
        #Existing head one value
        if self.head is self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return val
        #Existing head more than one
        #save old head value to return
        old_head = self.head
        #update head field to next node
        self.head = self.head.next
        #update new head's prev to none
        self.head.prev = None
        self.length -= 1
        return old_head


            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            old_tail = self.tail
            self.tail = new_node
            old_tail.next = self.tail
            self.tail.prev = old_tail
            self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return
        elif self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            val = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if head do nothing
        if self.length <= 1 or self.head == node:
            return
        #if tail call remove from tail
        elif node == self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
        else:
            self.length -= 1
            prev = self.find_prev(node)
            #prev node's .next point to next node
            prev.next = node.next
            #next node's .prev point to prev node
            node.next.prev = prev
            #add to front
            self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length <= 1 or self.tail == node:
            return
        elif node == self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            self.length -= 1
            prev = self.find_prev(node)
            prev.next = node.next
            node.next.prev = prev
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head:
            return None
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            prev = self.find_prev(node)
            prev.next = node.next
            node.next.prev = prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    def find_prev(self, node):
        if self.length == 0:
            return False
        current = self.head.next
        while current.next is not node and current.next:
            current = current.next
        return current
