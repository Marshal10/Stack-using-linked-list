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
        
    def __str__(self):
        if self.isEmpty():
            return "The stack is empty"
        values=[str(x.value) for x in self.linked_list]
        return '\n'.join(values)
        
    def isEmpty(self):
        if self.linked_list.head is None:
            return True
        return False
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.linked_list.head
        self.linked_list.head=new_node
    
customStack=Stack()
print(customStack.isEmpty())
print(customStack)
customStack.push(10)
customStack.push(11)
customStack.push(12)
print(customStack)