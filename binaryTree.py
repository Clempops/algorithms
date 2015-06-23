class BinaryTree():
  def __init__(self, rootObj):
    self.key = rootObj
    self.left = None
    self.right = None

  def insertLeft(self, newNode):
    if self.left == None:
      self.left = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.left = self.left
      self.left = t

  def insertRight(self, newNode):
    if self.right == None:
      self.right = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.right = self.right
      self.right = t

# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeft())
# r.insertLeft('b')
# print(r.getLeft())
# print(r.getLeft().getRootVal())
# r.insertRight('c')
# print(r.getRight())
# print(r.getRight().getRootVal())
# r.getRight().setRootVal('hello')
# print(r.getRight().getRootVal())

