import unorderedLinkedList

mylist = unorderedLinkedList.UnorderedList()

mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(3)
mylist.add(2)
mylist.add(1)

def isPalindrom(mylist):
  slow = mylist.head
  fast = mylist.head
  stack = []
  while fast != None:
    stack.append(slow.data)
    fast = fast.next
    if fast != None:
      slow = slow.next
      fast = fast.next
  while slow != None:
    if slow.data != stack.pop(): return False
    slow = slow.next
  return True

print isPalindrom(mylist)
  