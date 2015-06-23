class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    
  def add(self, data):
    current = self.head
    previous = None
    found = False
    while current != None and not found:
      if data > current.data:
        previous = current
        current = current.next
      else:
        found = True
    node = Node(data)
    if previous == None:
      self.head = node
      node.next = current
    else:
      if current != None:
        previous.next = node
        if current != None: node.next = current
      else:
        previous.next = node
    
  def search(self, data):
    current = self.head
    found = False
    end = False
    while not found and not end and current != None:
      if data == current.data:
        found = current.data
      else:
        if data < current.data:
          end = True
        else:
          current = current.next
    return found
    
mylist = LinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.search(31))
