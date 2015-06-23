import binaryTree

tree = binaryTree.BinaryTree(20)
tree.insertLeft(10)
tree.insertRight(30)
tree.left.insertLeft(8)
tree.left.insertRight(25)
tree.right.insertLeft(22)

def isSearch(node, mini = 0, maxi = 100):
  if node != None:
    if node.key <= mini or node.key >= maxi:
      return False
    return isSearch(node.left, mini, node.key) and isSearch(node.right, node.key, maxi)
  else: return True

print isSearch(tree)