"""
Queue Class
Included here: Day 18 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from PackageLinkedLists.Class_LinkedList import LinkedList

#implementing a queue via a linked list
#there are other ways to do this
class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def IsEmpty(self):
        return super().IsEmpty()

    #returns end index + 1
    def GetLength(self):
        return super().GetLength()

    #add to front, push other things to back
    def Enqueue(self,n):
        super().InsertAtStart(n)

    #pop things out the back
    def Dequeue(self):
        end_idx = super().GetLength() - 1
        super().RemoveAtIdx(end_idx)

    #look at the next item that can be removed from the queue
    def Peek(self):
        end_idx = super().GetLength() - 1
        node = super().GetNode(end_idx)
        print(f'The next item in the queue is: {node.head}')
        return node.head


        
#Testing Capability, making sure it had FIFO behavior
myQueue1 = Queue()
myQueue1.Enqueue(10)
myQueue1.Enqueue(20)
myQueue1.Enqueue(30)
myQueue1.PrintHeads()
myQueue1.Dequeue()
myQueue1.PrintHeads()
myQueue1.Peek()


myQueue2 = Queue()
myQueue2.Enqueue('Freddy')
myQueue2.Enqueue('Dalia')
myQueue2.Enqueue('Drew')
myQueue2.Enqueue('Yan')
myQueue2.PrintHeads()
myQueue2.Dequeue()
myQueue2.PrintHeads()
myQueue2.Peek()