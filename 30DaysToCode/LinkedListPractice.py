"""
Linked List Practice, Contains Node and Linked List Classes
Included here: Day 15 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

class Node:
    def __init__(self,head,tail = None):
        self.head = head
        self.tail = tail


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
    def RemoveAtIdx(self,idx):
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
            
        
#Creating an empty linked list
ll1 = LinkedList()

#creating independent nodes with empty tails
nodeA = Node(5)
nodeB = Node(10)
nodeC = Node(15)

#linking the nodes in a linked list
ll1.first = nodeA
nodeA.tail = nodeB
nodeB.tail = nodeC

#accessing the node heads through dot indexing the linked list
print('Head of the linked list:',ll1.first.head)
print('Head of second node in linked list:', ll1.first.tail.head)
print('Head of third node in linked list:', ll1.first.tail.tail.head)

ll1.PrintHeads()
print(f'The length of the list is {ll1.GetLength()}')

#Inserting a node at the start of the linked list
ll1.InsertAtStart(1)
ll1.PrintHeads()

#Inserting a node at the end of the linked list
ll1.InsertAtEnd(20)
ll1.PrintHeads()

#Inserting a node at the given index
ll1.InsertAtIdx(55,2)
ll1.PrintHeads()

#Retrieving the node at the given index
print('Head of node 0 is:', (ll1.GetNode(0)).head)
print('Head of node 2 is:', (ll1.GetNode(2)).head)

#New list, insert value at start
ll2 = LinkedList()
ll2.InsertAtStart(2)
ll2.PrintHeads()

#New List, converts list to linked List
ll3 = LinkedList()
myList = ['freddy', 'Dalia', 420, 69, 420.69]
for i in range(0,5):
    ll3.InsertAtStart(myList[i])
ll3.PrintHeads()
ll3.RemoveAtIdx(0)
ll3.PrintHeads()
