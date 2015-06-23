import binarySearchTree

tree = binarySearchTree.binarySearchTree()

tree[7] = 7
tree[3] = 3
tree[12] = 12
tree[2] = 2
tree[4] = 4
tree[10] = 10
tree[14] = 14

def findAncestor(A, B, tree):
  if A == B:
    return False
  current = tree.root
  deviation = False
  while not deviation and current != None:
    if current.key < A and current.key < B:
      current = current.right
    elif current.key > A and current.key > B:
      current = current.left
    else:
      deviation = current.key
  return deviation
    
print findAncestor(14, 10, tree)