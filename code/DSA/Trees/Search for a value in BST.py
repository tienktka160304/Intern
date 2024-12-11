class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def Searching(node, value):
    if node is None:
        return None
    elif node.data == value:
        return value
    elif value > node.data:
        return Searching(node.right, value)
    else:
        return Searching(node.left, value)
    
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.right = node15
root.left = node7

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

target = 20
if Searching(root, target):
    print("found")
else:
    print("nope")
