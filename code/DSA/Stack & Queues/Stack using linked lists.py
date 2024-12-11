class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head #the next pointer of new node is set to point to the current head
        self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            return "Empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def Size(self):
        return self.size

myStack = Stack()
#push
myStack.push('A')
myStack.push('d')
myStack.push('e')

#pop
print(myStack.pop())

#isEmpty
print(myStack.isEmpty())

#Peek
print(myStack.peek())

#Size
print(myStack.Size())