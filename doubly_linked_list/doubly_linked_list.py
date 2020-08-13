"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
import gc


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
        newNode = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head  
            self.head.prev = newNode  
            self.head = newNode  


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        deleHead = self.head
        newHead = deleHead.next
        if newHead:
            newHead.prev = None
            self.head = newHead
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return deleHead.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newTail = ListNode(value, None, None)
        # add value of 1 to list
        self.length += 1
        # check if list is empty
        if not self.head and not self.tail:
            self.head = newTail
            self.tail = newTail
        else:
            # points to new node
            newTail.prev = self.tail
            # new node becomes new tail
            self.tail.next = newTail
            self.tail = newTail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        delTail = self.tail
        if delTail == None:
            return None
        newNode = delTail.prev
        if newNode:
            newNode.next = None
            self.tail = newNode
        else:
            self.head, self.tail = None, None
        self.length -= 1
        return delTail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        temp = self.head
        self.head = node
        self.head.next = temp
        self.head.prev = None
        temp.prev = self.head
        self.length += 1
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        self.length += 1

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node.prev == None:
            self.remove_from_head()
        elif node.next == None:
            self.remove_from_tail()
        else:
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev
            self.length -= 1




    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_val = float("-inf")
        node = self.head
        while node != None:
            if node.value > max_val:
                max_val = node.value
            node = node.next
        return max_val
