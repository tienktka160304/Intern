class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def TraverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=' -> ')
        currentNode = currentNode.next
    print('null')
    
def InsertANode(head, NewNode, position):
    if position == 1:   #if newnode at the head
        NewNode.next = head
        return NewNode
    currentNode = head
    for _ in range(position - 2):   #traverse to the desired position ( vtri mong muon)
        if currentNode is None: 
            break
        currentNode = currentNode.next
        
    NewNode.next = currentNode.next #currentNode.next sẽ có vị trí là NewNode.next
    currentNode.next = NewNode  # NewNode sẽ có vị trí của CurrentNode
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("before : ")
TraverseAndPrint(node1)

newNode = Node(78)
InsertANode(node1, newNode, 2)

print("after:")
TraverseAndPrint(node1)