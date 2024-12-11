class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None  #the end of the queue (the position an element just added)
        self.length = 0
        
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:   #if the queue is empty
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return 'Empty'
        temp = self.front   #store
        self.front = temp.next  #move pointer
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
        
    def peek(self):
        if self.isEmpty():
            return 'Empty'
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def Size(self):
        return self.length
    
    def Print(self):
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()  #\n

myQueue = Queue()

myQueue.enqueue('a')
myQueue.enqueue('s')
myQueue.enqueue('f')
myQueue.Print()

#dequeue
print(myQueue.dequeue())

#peek
print(myQueue.peek())

#isEmpty
print(myQueue.isEmpty())

#Size
print(myQueue.Size())
