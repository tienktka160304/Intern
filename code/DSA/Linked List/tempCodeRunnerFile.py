print(". . .")    

print("\nBackward:")
cucurrentNode = node4
startNode = node4
print(currentNode.data, end='->')
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end='->')
    currentNode = currentNode.prev
print(". . .")    
