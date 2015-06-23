import binarySearchTree

tree = binarySearchTree.binarySearchTree()

tree[7] = 'a'
tree[3] = 'b'
tree[12] = 'c'
tree[2] = 'd'
tree[4] = 'e'
tree[10] = 'f'
tree[14] = 'g'
  
levels = {}
def Levels(node, level = 0):
  if node != None:
    level += 1
    if level in levels:
      levels[level].append(node.key)
    else: 
      levels[level] = [node.key]
    Levels(node.left, level)
    Levels(node.right, level)
  return levels

print Levels(tree.root)