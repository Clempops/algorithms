import binarySearchTree
import levelLists

def child_binary_tree(binary_tree, node, alist):
  if len(alist) > 0:
    mid_pos = len(alist) // 2
    if node == None: 
      binary_tree.root = binarySearchTree.Node(alist[mid_pos], alist[mid_pos])
      node = binary_tree.root
    else:
      node.key = alist[mid_pos]
      node.data = alist[mid_pos]
    if alist[:mid_pos] != []:
      node.left = binarySearchTree.Node(0, 0, parent=node)
      child_binary_tree(binary_tree, node.left, alist[:mid_pos])
    if alist[mid_pos+1:] != []:
      node.right = binarySearchTree.Node(0, 0, parent=node)
      child_binary_tree(binary_tree, node.right, alist[mid_pos+1:])

binaryTree = binarySearchTree.binarySearchTree()
child_binary_tree(binaryTree, binaryTree.root, range(10))
lists = levelLists.Levels(binaryTree)