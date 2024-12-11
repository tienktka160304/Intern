class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        self.queue.append(element)
        
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        return self.queue.pop(0)
    
    def Peek_element(self):
        if self.isEmpty():
            return "Empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def Size(self):
        return len(self.queue)

myQueue = Queue()
# Enqueue
myQueue.enqueue('a')
myQueue.enqueue('s')
myQueue.enqueue('f')
print(myQueue)

#dequeue
print(myQueue.dequeue())

#peek
print(myQueue.Peek_element())

#isEmpty
print(myQueue.isEmpty())

#Size
print(myQueue.Size())
