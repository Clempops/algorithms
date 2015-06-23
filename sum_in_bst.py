import binarySearchTree

tree = binarySearchTree.binarySearchTree()

tree[7] = 7
tree[3] = 3
tree[12] = 12
tree[2] = 2
tree[4] = 4
tree[10] = 10
tree[14] = 14

def findSum(path, summ, node):
  if node != None:
    path.append(node.value)
    t = []
    for i in reversed(path):
      t += [i]
      if sum(t) == summ: print t
    
    findSum(path, summ, node.left)
    findSum(path, summ, node.right)
    
findSum([], 12, tree.root)