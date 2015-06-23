class Node:
  def __init__(self, key, value, parent=None, left=None, right=None):
    self.parent = parent
    self.left = left
    self.right = right
    self.value = value
    self.key = key

class binarySearchTree:
  def __init__(self, root=None):
    self.root = root
    
  def __getitem__(self, key):
    if self.root == None:
      return 'empty'
    else:
      found = False
      current = self.root
      while not found:
        if key == current.key:
          found = True
          print current.value
        elif key < current.key:
          if current.left != None:
            current = current.left
          else:
            found = True
            print 'does not exists'
        else:
          if current.right != None:
            current = current.right
          else:
            found = True
            print 'does not exists'
        
  def __setitem__(self, key, value):
    if self.root == None:
      self.root = Node(key, value)
    else:
      found = False
      current = self.root
      while not found:
        if key == current.key:
          current.value = value
          found = True
        elif key < current.key:
          if current.left != None:
            current = current.left
          else:
            current.left = Node(key, value, parent=current)
            found = True
        else:
          if current.right != None:
            current = current.right
          else:
            current.right = Node(key, value, parent=current)
            found = True
        

mytree = binarySearchTree()
mytree[1] = 'word1'
mytree[2] = 'word2'
mytree[4] = 'word4'
mytree[3] = 'word3'