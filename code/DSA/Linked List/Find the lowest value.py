class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
def FindTheLowestValue(head):
    currentNode = head
    min_value = head.data
    while currentNode:
        if currentNode.data < min_value:
            min_value = currentNode.data
        currentNode = currentNode.next
    return min_value
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(FindTheLowestValue(node1))