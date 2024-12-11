class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def Delete(node, data):
    if not node:
        return None
    if data < node.data:
        node.left = Delete(node.left, data)
    elif data > node.data:
        node.right = Delete(node.right, data)
    else:
#check node with only 1 child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        
#node with 2 children, get inOrder successor
        node.data = minValue(node.right).data
        node.right = Delete(node.right, node.data)
    return node

def InOrder(node):
    if node:
        InOrder(node.left)
        print(node.data, end=', ')
        InOrder(node.right)
        
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

Delete(root, 13)

InOrder(root)