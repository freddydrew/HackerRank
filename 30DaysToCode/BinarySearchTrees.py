"""
Binary Search Trees
Included here: Day 22 of 30 Days to Code.
See the Jupyter Notebook for more notes related to this tutorial.
"""

from random import randint

class Node:
    def __init__(self,Value=None):
        self.Value=Value
        self.LeftChild=None #pointer
        self.RightChild=None #pointer


class BST:
    def __init__(self):
        self.Root=None


    def Insert(self,Value):
        #first, can I insert this at the root
        if self.Root==None:
            self.Root=Node(Value)
        else:
            self._Insert(Value,self.Root)

    #this is recursive, best to seperate from other insert function
    def _Insert(self,Value,CurrentNode):
        if Value < CurrentNode.Value or Value == CurrentNode.Value:
            if CurrentNode.LeftChild == None:
                CurrentNode.LeftChild = Node(Value)
            else:
                self._Insert(Value,CurrentNode.LeftChild)
        elif Value > CurrentNode.Value:
            if CurrentNode.RightChild == None:
                CurrentNode.RightChild = Node(Value)
            else:
                self._Insert(Value,CurrentNode.RightChild)
        #What do we do with repeat values???
        else:
            print(f'{Value} already in the tree!')

    def PrintTree(self):
        if self.Root != None:
            self._PrintTree(self.Root)

    def _PrintTree(self,CurrentNode):
        if CurrentNode != None:
            self._PrintTree(CurrentNode.LeftChild)
            print(str(CurrentNode.Value))
            self._PrintTree(CurrentNode.RightChild)

    def Height(self):
        if self.Root == None:
            return 0
        else:
            return self._Height(self.Root,0)

    def _Height(self,CurrentNode,CurrentHeight):
        if CurrentNode == None:
            return CurrentHeight
        else:
            LeftHeight = self._Height(CurrentNode.LeftChild,CurrentHeight+1)
            RightHeight = self._Height(CurrentNode.RightChild,CurrentHeight+1)
            return max(LeftHeight,RightHeight)

    def Search(self,Value):
        if self.Root == None:
            return False
        else:
            return self._Search(self.Root,Value)

    def _Search(self,CurrentNode,Value):
        if CurrentNode.Value == Value:
            return True
        elif Value <= CurrentNode.Value and CurrentNode.LeftChild != None:
            return self._Search(CurrentNode.LeftChild,Value)
        elif Value > CurrentNode.Value and CurrentNode.RightChild != None:
            return self._Search(CurrentNode.RightChild,Value)    
        return False

def _FillTree(Tree,NumElements=100,MaxInt=1000):
    for _ in range(NumElements):
        CurrentElement = randint(0,MaxInt)
        Tree.Insert(CurrentElement)
    return Tree


MyBST = BST()
MyBST = _FillTree(MyBST)
MyBST.PrintTree()
print(MyBST.Height())
MyBST.Insert(420)
print(MyBST.Search(420))













