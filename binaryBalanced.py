import binarySearchTree

tree = binarySearchTree.binarySearchTree()

tree[10]="red"
tree[18]="blue"
tree[4]="yellow"
tree[2]="at"
tree[6]="red"
tree[1]="red"
tree[12]="blue"

levelSet = set([])
def isBalanced(node, level = 0):
  print levelSet
  if node != None:
    level += 1
    isBalanced(node.left, level)
    isBalanced(node.right, level)
  else:
      levelSet.add(level)
  return len(levelSet)

print isBalanced(tree.root)