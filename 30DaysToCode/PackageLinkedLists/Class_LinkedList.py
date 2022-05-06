"""
Linked List Class
Included here: Day 18 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""
from PackageLinkedLists.Class_Node import Node

class LinkedList:
    def __init__(self):
        self.first = None

    #Print the heads of the linked list's nodes
    def PrintHeads(self):
        node = self.first
        print('Printing the heads of the linked list nodes:')
        count = 0
        while node is not None:
            print(f'Node {count} head =',node.head)
            node = node.tail
            count += 1
        print('Done printing the heads of the linked list nodes.')

    #Return the length of the linked list
    def GetLength(self):
        node = self.first
        count = 0
        while node is not None:
            node = node.tail
            count += 1
        return count
    
    #Find out if the list is empty or not
    def IsEmpty(self):
        if self.first == None:
            print('This sequence is empty.')
        print('This sequence is not empty.')

    #Returning the Node at a given index
    def GetNode(self,idx):
        node = self.first
        count = 0
        if count == idx:
            return node
        while (count < idx):
            node = node.tail
            count += 1
        return node


    #Insert New Node at Start of Linked List
    def InsertAtStart(self,val):
        NewNode = Node(val)
        NewNode.tail = self.first
        self.first = NewNode

    #Inserting a new node at the end of the linked list
    def InsertAtEnd(self,val):
        NewNode = Node(val)
        node = self.first
        while node.tail:
            node = node.tail
        node.tail = NewNode

    #Inserting a new node at the given idx
    def InsertAtIdx(self,val,idx):
        NewNode = Node(val)
        count = 0
        node = self.first
        while(count < (idx-1)):
            node = node.tail
            count += 1
        NewNode.tail = node.tail
        node.tail = NewNode

    #Removing node at a given index
    #does start, end, and inbetween
    def RemoveAtIdx(self,idx = 0):
        if idx == 0:
            self.first = self.first.tail
        count = 0
        node = self.first
        prevNode = node
        while node.tail is not None:
            node = node.tail
            count += 1
            if count == (idx - 1):
                prevNode = node
            if count > idx:
                prevNode.tail = node
                break
            if node.tail == None:
                prevNode.tail = None