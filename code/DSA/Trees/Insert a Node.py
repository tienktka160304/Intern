class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def Insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = Insert(node.left, data)
        elif data > node.data:
            node.right = Insert(node.right, data)
    return node

def InOrderBT(node):
    if node is None:
        return
    InOrderBT(node.left)
    print(node.data, end =', ')
    InOrderBT(node.right)
    
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

index = int(input())

Insert(root, index)

InOrderBT(root)