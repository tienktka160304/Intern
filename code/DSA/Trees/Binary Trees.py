class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA

nodeA.left = nodeC
nodeA.right = nodeD

root.right = nodeB

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print('root.right.left.data =', root.right.left.data)
