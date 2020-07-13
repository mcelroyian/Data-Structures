class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        # 1. create node from value
        new_node = Node(value)
        if self.tail is None and self.head is None:
            self.head = new_node
            # set the new node to be the tail
            self.tail = new_node
        else:
            # 2. set old tail to refer to new node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node
    
    def remove_tail(self):

        if self.head is None and self.tail is None:
            return 

        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()
        # if non empty
        # set tail to none
        val = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)


        return val

    def remove_head(self):
        if self.head is None and self.tail is None:
            return 

        if not self.head.get_next():
            head = self.head.get_value()
            self.head = None
            self.tail = None
            return head

        val = self.head.get_value()

        self.head = self.head.get_next()

        return val

    def contains(self, value):
        if not self.head:
            return False
        current = self.head

        while current:
            if current.get_value() == value:
                return True
            
            current = current.get_next()

        return False

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()

        current = self.head.get_next()

        while current:

            if current.get_value() > max_value:
                max_value = current.get_value()

            current = current.get_next()
        
        return max_value

    def is_empty(self):
        return self.head == None and self.tail == None
        
