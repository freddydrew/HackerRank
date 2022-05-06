"""
Stack Practice
Included here: Day 18 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

####making a stack with a list
ListStack = []
print('List Stack after instatiation: ',ListStack) 

#showing off Lifo behavior
ListStack.append('a') #first in
print('List Stack after 1 push: ',ListStack) 
ListStack.append('b') #second in
print('List Stack after 2 pushes: ',ListStack) 
ListStack.append('c') #third in (last in)
print('List Stack after 3 pushes: ',ListStack) 

ListStack.pop() #removes third in
print('List Stack after 1 pop: ',ListStack) 
fred = ListStack.pop() #removes second in
print('List Stack after 2 pops: ',ListStack) 
ListStack.pop() #removes first in
print('List Stack after 3 pops: ',ListStack) 

####making a stack with collections.deque
from collections import deque
DequeStack = deque()
print('Collection.deque Stack after instatiation: ',DequeStack) 

#showing off Lifo behavior
DequeStack.append('a') #first in
print('Collection.deque Stack after 1 push: ',DequeStack) 
DequeStack.append('b') #second in
print('Collection.deque Stack after 2 pushes: ',DequeStack) 
DequeStack.append('c') #third in (last in)
print('Collection.deque Stack after 3 pushes: ',DequeStack) 
DequeStack.pop() #removes third in
print('Collection.deque Stack after 1 pop: ',DequeStack) 
DequeStack.pop() #removes second in
print('Collection.deque Stack after 2 pops: ',DequeStack) 
DequeStack.pop() #removes first in
print('Collection.deque Stack after 3 pops: ',DequeStack) 

####making a stack with queue.LifoQueue
from queue import LifoQueue
LifoQueueStack = LifoQueue()
print('queue.LifoQueue Stack size after instatiation: ',LifoQueueStack.qsize()) 

#showing off Lifo behavior
LifoQueueStack.put('a') #first in
print('queue.LifoQueue Stack size after 1 push: ',LifoQueueStack.qsize()) 
LifoQueueStack.put('b') #second in
print('queue.LifoQueue Stack size after 2 pushes: ',LifoQueueStack.qsize()) 
LifoQueueStack.put('c') #third in (last in)
print('queue.LifoQueue Stack size after 3 pushes: ',LifoQueueStack.qsize()) 
LifoQueueStack.get() #removes third in
print('queue.LifoQueue Stack size after 1 pop: ',LifoQueueStack.qsize()) 
LifoQueueStack.get() #removes second in
print('queue.LifoQueue Stack size after 2 pops: ',LifoQueueStack.qsize()) 
LifoQueueStack.get() #removes first in
print('queue.LifoQueue Stack size after 3 pops: ',LifoQueueStack.qsize()) 

####making a stack with singly linked list
from PackageLinkedLists.Class_LinkedList import LinkedList
LinkedListStack = LinkedList()
letters = ['a', 'b', 'c']
count = 0
for letter in letters:
    LinkedListStack.InsertAtStart(letter)
    print(f'Linked List Stack after push {count}',LinkedListStack.PrintHeads())

count = 0
for i in range(0,2):
    LinkedListStack.RemoveAtIdx()
    print(f'Linked List Stack after pop {count}',LinkedListStack.PrintHeads())