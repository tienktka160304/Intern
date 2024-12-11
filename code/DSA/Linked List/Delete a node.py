class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def TraverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=' -> ')
        currentNode = currentNode.next
    print("null")
    
def DeleteANode(head, SpecificNode):
    if head == SpecificNode:    # if specify first node
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != SpecificNode: #traverse the list
        currentNode = currentNode.next
        
    if currentNode.next is None:    #check if the specific node is none
        return head
    
    currentNode.next = currentNode.next.next    #Delete the specific node (ex: n1 = n2)
    
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

DeleteANode(node1, node1)
print("after:")
TraverseAndPrint(node1)