class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
            
class Stack:
    def __init__(self):
        self.linked_list=LinkedList()
        
    def isEmpty(self):
        if self.linked_list.head is None:
            return True
        return False
    
customStack=Stack()
print(customStack.isEmpty())