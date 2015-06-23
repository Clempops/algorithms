def schoolAdd(a, b):
  A = a.head
  B = b.head
  C = UnorderedList()
  remainder = 0
  while A != None and B != None:
    res = A.data + B.data + remainder
    if res > 9:
      remainder = 1
      C.add(res % 10)
    else:
      remainder = 0
      C.add(res)
    A = A.next
    B = B.next
  i = C.head
  while i != None:
    print i.data
    i = i.next