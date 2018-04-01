#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 2                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	10/2/2018           #
#############################################
"""
Description：
Task1:
Write a definition for the append() function of the LinkedList class.
This function should add the value at the end of the linked list and must
do this such that the time complexity of the operation is O(1).
Task2:
Re-write the definition for the size() function of the LinkedList class.
This function should return the total number of values in the Linked List
and must do this such that the time complexity of the operation is
O(1).
"""
class Node:
    def __init__(self, new_value):
        self.value = new_value
        self.next = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_value(self, new_value):
        self.value = new_value

    def set_next_node(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.set_next_node(self.head)
            self.head = new_node
        self.count += 1
        
    def append(self, value):
        ##You need to implement this function to work in O(1) time.
        ##Don't forget to also change the other necessary functions.
        new_node = Node(value)
        if self.head ==None:
            self.head =new_node
        else:
             self.tail.set_next_node(new_node)
        self.tail = new_node
        self.count += 1

    def remove(self,value):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_value() == value:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if found:
            if previous == None:
                self.head = current.get_next_node()
            else:
                previous.set_next_node(current.get_next_node())
                self.tail =previous
        self.count -= 1

    def size(self):
        ##You need to re-write this method to work in O(1) time
        ##Don't forget to change the other necessary functions
        
        return self.count

    def to_list(self):
        current = self.head
        my_list = []
        while current != None:
            my_list.append(current.get_value())
            current = current.get_next_node()
        return my_list


my_list= LinkedList()
my_list.add(6)
my_list.add(5)
my_list.add(4)
my_list.add(3)
my_list.add(2)
my_list.remove(6)
my_list.append(7)
print(my_list.to_list())
print(my_list.size())



