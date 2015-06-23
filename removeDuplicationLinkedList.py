import unorderedLinkedList

mylist = unorderedLinkedList.UnorderedList()

mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(1)
mylist.add(4)
mylist.add(1)

pool = []

def removeDuplicationLinkedList(alist):
  if alist.head == None: return False
  node = alist.head
  previous = None
  while node != None:
    if node.data in pool:
      previous.next = node.next
      node = previous.next
    else:
      pool.append(node.data)
      previous = node
      node = node.next
  return alist
  
mylist = removeDuplicationLinkedList(mylist)

node = mylist.head
while node != None: 
  print node.data
  node = node.next